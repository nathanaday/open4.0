import os
from datetime import datetime, timedelta, timezone
import json

from fastapi import FastAPI, HTTPException, Request, Path, Depends, status, Body
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import jwt as pyjwt
from passlib.context import CryptContext
from jose import JWTError, jwt
from dotenv import load_dotenv

from pydantic import BaseModel
import logging
import uvicorn

from persistence.FlexData import RedisDatabase
from persistence.components.Redis import RedisClient
from persistence.components.DatabaseInterface import DatabaseInterface


class AppManager:
    def __init__(self, db: DatabaseInterface):
        self.db = db

    def add_device(self, device_id: str, device_info: dict):
        self.db.save_device(device_id, device_info)

    def get_device(self, device_id: str):
        return self.db.get_device(device_id)

    def delete_device(self, device_id: str):
        self.db.delete_device(device_id)

    def add_group(self, group_id: str, group_info: dict):
        self.db.save_group(group_id, group_info)

    def get_group(self, group_id: str):
        return self.db.get_group(group_id)

    def log_event(self, event_info: dict):
        self.db.log_event(event_info)

    def get_events(self, device_id: str):
        return self.db.get_events(device_id)


class Open40API:

    def __init__(self):
        # Initialize FastAPI rest api backend application
        self.app = FastAPI()

        # CORS setup
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        redis_client = RedisClient()

        print(redis_client.client)
        print(type(redis_client.client))

        self.db = RedisDatabase(redis_client)
        self.app_manager = AppManager(self.db)

        # Register routes
        self.app.get("/")(self.home)
        self.app.post("/devices")(self.add_device)
        self.app.get("/devices/{device_id}")(self.get_device)
        self.app.delete("/devices/{device_id}")(self.delete_device)
        self.app.post("/groups")(self.add_group)
        self.app.get("/groups/{group_id}")(self.get_group)
        self.app.post("/events")(self.log_event)
        self.app.get("/events/{device_id}")(self.get_events)

    async def home(self):
        return {"message": "Hello!"}

    async def add_device(self, device_id: str = Body(...), device_info: dict = Body(...)):
        self.app_manager.add_device(device_id, device_info)
        return {"message": "Device added successfully"}

    async def get_device(self, device_id: str = Path(...)):
        device = self.app_manager.get_device(device_id)
        if not device:
            raise HTTPException(status_code=404, detail="Device not found")
        return device

    async def delete_device(self, device_id: str = Path(...)):
        self.app_manager.delete_device(device_id)
        return {"message": "Device deleted successfully"}

    async def add_group(self, group_id: str = Body(...), group_info: dict = Body(...)):
        self.app_manager.add_group(group_id, group_info)
        return {"message": "Group added successfully"}

    async def get_group(self, group_id: str = Path(...)):
        group = self.app_manager.get_group(group_id)
        if not group:
            raise HTTPException(status_code=404, detail="Group not found")
        return group

    async def log_event(self, event_info: dict = Body(...)):
        self.app_manager.log_event(event_info)
        return {"message": "Event logged successfully"}

    async def get_events(self, device_id: str = Path(...)):
        events = self.app_manager.get_events(device_id)
        if not events:
            raise HTTPException(status_code=404, detail="No events found for this device")
        return events


if __name__ == "__main__":
    open40 = Open40API()
    uvicorn.run(open40.app, host='0.0.0.0', port=5050, log_level="debug")

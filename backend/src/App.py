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

        # Register routes
        self.app.get("/")(self.home)

    async def home(self):
        return "Hello!"


if __name__ == "__main__":
    open40 = Open40API()
    uvicorn.run(open40.app, host='0.0.0.0', port=5050, log_level="debug")

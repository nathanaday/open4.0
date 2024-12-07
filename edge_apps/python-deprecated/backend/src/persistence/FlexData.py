from persistence.components.DatabaseInterface import DatabaseInterface
from persistence.components.Redis import RedisClient


class RedisDatabase(DatabaseInterface):
    def __init__(self, redis_client: RedisClient):
        self.redis_client = redis_client

    def save_device(self, device_id: str, device_info: dict):
        self.redis_client.hset(f"device:{device_id}", mapping=device_info)

    def get_device(self, device_id: str):
        return self.redis_client.hgetall(f"device:{device_id}")

    def delete_device(self, device_id: str):
        self.redis_client.delete(f"device:{device_id}")

    def save_group(self, group_id: str, group_info: dict):
        self.redis_client.set(f"group:{group_id}", group_info)

    def get_group(self, group_id: str):
        return self.redis_client.get(f"group:{group_id}")

    def log_event(self, event_info: dict):
        event_id = event_info["event_id"]
        device_id = event_info["device_id"]
        self.redis_client.append_to_list(f"events:{device_id}", event_info)

    def get_events(self, device_id: str):
        return self.redis_client.get_list(f"events:{device_id}")

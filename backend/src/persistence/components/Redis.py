import redis
import json


class RedisClient:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.StrictRedis(host=host, port=port, db=db)

    def set(self, key, value):
        self.client.set(key, json.dumps(value))

    def get(self, key):
        value = self.client.get(key)
        return json.loads(value) if value else None

    def delete(self, key):
        self.client.delete(key)

    def append_to_list(self, key, value):
        self.client.rpush(key, json.dumps(value))

    def get_list(self, key):
        values = self.client.lrange(key, 0, -1)
        return [json.loads(value) for value in values]

    def hset(self, name, mapping):
        serialized_mapping = {k: json.dumps(v) if isinstance(v, (dict, list)) else v for k, v in mapping.items()}
        self.client.hset(name, mapping=serialized_mapping)

    def hgetall(self, name):
        raw_data = self.client.hgetall(name)
        return {k.decode('utf-8'): json.loads(v.decode('utf-8')) if v.decode('utf-8').startswith(
            ('{"', '[', '"')) else v.decode('utf-8') for k, v in raw_data.items()}

from appdirs import user_cache_dir
from redis_dict import RedisDict
from redis import Redis
import redis_lock
import pathlib
import json
from contextlib import contextmanager

CACHE_PATH = user_cache_dir("tiny_cache", "tiny_cache")
from pottery import Redlock


class RedisConnection:
    def __init__(self) -> None:
        self.redis_config = self.redis_config()

    @contextmanager
    def get_queue(self): 
        db = RedisDict(**self.redis_config)
        redis = Redis(**self.redis_config)
        lock = Redlock(key='queue', masters={redis})
        with lock:
            try:
                yield db
            finally:
                pass
        # return lock,db
        # with  db.expire_at(None):
            
    @staticmethod
    def redis_config():
        assert pathlib.Path(f"{CACHE_PATH}/redis_config.json").exists(), "Please run tiny_queue login"
        with open(f"{CACHE_PATH}/redis_config.json") as f:
            return json.load(f)
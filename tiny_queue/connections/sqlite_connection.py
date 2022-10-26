
from appdirs import user_cache_dir
from contextlib import contextmanager
from sqlitedict import SqliteDict
from filelock import FileLock

CACHE_PATH = user_cache_dir("tiny_cache", "tiny_cache")

class SqliteConnection:
    def __init__(self) -> None:
        pass
    
    @contextmanager
    def get_queue(self):
        lock  = FileLock(f"{CACHE_PATH}/queue_database.bin.lock")
        db = SqliteDict(f"{CACHE_PATH}/queue_database.bin", autocommit=True)
        with lock,db:
            try:
                yield db
            finally:
                pass
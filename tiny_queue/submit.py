from appdirs import user_cache_dir
from sqlitedict import SqliteDict
from filelock import FileLock
from loguru  import logger
from redis_dict import RedisDict

CACHE_PATH = user_cache_dir("tiny_cache", "tiny_cache")

def submit_task(task, queue="redis"):
    if queue=="sqlite":
        sqlite_submit_task(task)
    elif queue=="redis":
        redis_submit_task(task)
    else :
        raise ValueError("queue must be sqlite or redis")
        

def sqlite_submit_task(task):
    
    logger.info(f"{CACHE_PATH}/queue_database.bin.lock")
    lock = FileLock(f"{CACHE_PATH}/queue_database.bin.lock")
    queue_datebase = SqliteDict(f"{CACHE_PATH}/queue_database.bin", autocommit=True)
    with lock, queue_datebase:
        write_task(task, queue_datebase)
        
import pathlib
import json
def redis_config():
    assert pathlib.Path(f"{CACHE_PATH}/redis_config.json").exists(), "Please run tiny_queue login"
    with open(f"{CACHE_PATH}/redis_config.json") as f:
        return json.load(f)
    

def redis_submit_task(task):
    redis_config = redis_config()

    queue_datebase = RedisDict(**redis_config)
    write_task(task, queue_datebase)

def write_task(task, queue_datebase):
    logger.info(f"{len(queue_datebase)} items in the db")
    if b"queue" not in queue_datebase:
        queue_datebase[b'queue'] = []
        
    queue = queue_datebase[b'queue']
    queue.append(task)
    queue_datebase[b'queue'] = queue



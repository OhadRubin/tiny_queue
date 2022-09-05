from appdirs import user_cache_dir
from sqlitedict import SqliteDict
from filelock import FileLock
from loguru  import logger
import subprocess

cache_path = user_cache_dir("tiny_cache", "tiny_cache")
def get_next_task():
    while True:
        lock = FileLock(f"{cache_path}/queue_database.bin.lock")
        queue_datebase = SqliteDict(f"{cache_path}/queue_database.bin", autocommit=True)
        with lock, queue_datebase:
            
            if b"queue" in queue_datebase:
                queue = queue_datebase[b'queue']
                if len(queue)>0:
                    next_task = queue.pop()
                    queue_datebase[b'queue'] = queue
                    return next_task
def worker_loop():
    logger.info(f"Starting worker")
    while True:
        next_task = get_next_task()
        logger.info(f'Running task "{next_task}"')
        try:
            subprocess.check_call(next_task,shell=True)
        except:
            pass
        
        

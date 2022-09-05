from appdirs import user_cache_dir
from sqlitedict import SqliteDict
from filelock import FileLock
from loguru  import logger

cache_path = user_cache_dir("tiny_cache", "tiny_cache")


def write_task(task = "echo 'Hello World'"):
    logger.info(f'Writing task "{task}"')
    logger.info(f"{cache_path}/queue_database.bin.lock")
    lock = FileLock(f"{cache_path}/queue_database.bin.lock")
    queue_datebase = SqliteDict(f"{cache_path}/queue_database.bin", autocommit=True)
    with lock, queue_datebase:
        logger.info(f"{len(queue_datebase)} items in the db")
        if b"queue" not in queue_datebase:
            queue_datebase[b'queue'] = []
        
        queue = queue_datebase[b'queue']
        queue.append(task)
        queue_datebase[b'queue'] = queue
        print(queue_datebase[b'queue'])

from sqlitedict import SqliteDict
from filelock import FileLock
import os
os.environ["LOGURU_LEVEL"] = "INFO"
from loguru  import logger
import subprocess
from tiny_queue.connections.redis_connection import RedisConnection
from tiny_queue.connections.sqlite_connection import SqliteConnection
import time

from retry import retry

@retry(backoff=2, tries=10)
def get_queue(queue_datebase):
    queue = queue_datebase.pop(b'queue',[])
    return queue

def get_next_task(conn):
    logger.debug("Getting next task")
    while True:
        time.sleep(0.5)
        # lock,queue_datebase = 
        logger.debug("Before locking")
        # with lock,queue_datebase:
        # with queue_datebase:
        with conn.get_queue() as queue_datebase:
            logger.debug("After locking")
            # try:
                
                # if b"queue" in queue_datebase:
            queue = get_queue(queue_datebase)
            # .pop(b'queue',[])
            
            if len(queue)>0:
                next_task = queue.pop()
                queue_datebase[b'queue'] = queue
                return next_task
            # except:
            #     pass
                
def agent_loop(queue="redis"):
    logger.info(f"Starting agent")
    if queue=="sqlite":
        conn = SqliteConnection()
    elif queue=="redis":
        conn = RedisConnection()
    else:
        raise ValueError("queue must be sqlite or redis")
    logger.info("Starting agent loop")
    while True:
        next_task = get_next_task(conn)
        logger.info(f'Running task "{next_task}"')
        try:
            subprocess.check_call(next_task,shell=True)
        except:
            pass
        logger.info(f'Finished task "{next_task}"')
        
        

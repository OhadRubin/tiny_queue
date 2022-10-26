from sqlitedict import SqliteDict
from filelock import FileLock
from loguru  import logger
import subprocess
from tiny_queue.connections.redis_connection import RedisConnection
from tiny_queue.connections.sqlite_connection import SqliteConnection
import time


def get_next_task(conn):
    while True:
        time.sleep(1)
        with conn.get_queue() as queue_datebase:
            try:
                if b"queue" in queue_datebase:
                    queue = queue_datebase[b'queue']
                    if len(queue)>0:
                        next_task = queue.pop()
                        queue_datebase[b'queue'] = queue
                        return next_task
            except:
                pass
                
def agent_loop(queue="redis"):
    logger.info(f"Starting agent")
    if queue=="sqlite":
        conn = SqliteConnection()
    elif queue=="redis":
        conn = RedisConnection()
    else:
        raise ValueError("queue must be sqlite or redis")
    
    while True:
        next_task = get_next_task(conn)
        logger.info(f'Running task "{next_task}"')
        try:
            subprocess.check_call(next_task,shell=True)
        except:
            pass
        
        

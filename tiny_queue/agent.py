from sqlitedict import SqliteDict
from filelock import FileLock
from loguru  import logger
import subprocess
from tiny_queue.connections.redis import RedisConnection
from tiny_queue.connections.sqlite import SqliteConnection



def get_next_task(conn):
    while True:
        with conn.get_queue() as queue_datebase:
            if b"queue" in queue_datebase:
                queue = queue_datebase[b'queue']
                if len(queue)>0:
                    next_task = queue.pop()
                    queue_datebase[b'queue'] = queue
                    return next_task
                
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
        
        

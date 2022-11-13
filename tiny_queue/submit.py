
from loguru  import logger
from tiny_queue.connections.redis_connection import RedisConnection
from tiny_queue.connections.sqlite_connection import SqliteConnection
from retry import retry

#set loguru logger to a specified level
# def set_loguru_level(level):


# tiny_queue submit "echo hi"
@retry()
def write_task(task, conn):
    with conn.get_queue() as queue_datebase:
        logger.info(f"{len(queue_datebase)} items in the db")
        queue = queue_datebase.pop(b"queue",[])
        queue.append(task)
        queue_datebase[b'queue'] = queue



def submit_task(task, queue):
    
    if queue=="sqlite":
        conn = SqliteConnection()
    elif queue=="redis":
        conn = RedisConnection()
    else:
        raise ValueError("queue must be sqlite or redis")
    logger.info(f"Submitting task {task}")
    write_task(task, conn)
    
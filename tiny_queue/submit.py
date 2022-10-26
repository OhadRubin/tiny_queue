
from loguru  import logger
from tiny_queue.connections.redis import RedisConnection
from tiny_queue.connections.sqlite import SqliteConnection



def write_task(task, queue_datebase):
    logger.info(f"{len(queue_datebase)} items in the db")
    if b"queue" not in queue_datebase:
        queue_datebase[b'queue'] = []
        
    queue = queue_datebase[b'queue']
    queue.append(task)
    queue_datebase[b'queue'] = queue



def submit_task(task, queue="redis"):
    
    if queue=="sqlite":
        conn = SqliteConnection()
    elif queue=="redis":
        conn = RedisConnection()
    else:
        raise ValueError("queue must be sqlite or redis")
    with conn.get_queue() as queue_datebase:
        write_task(task, queue_datebase)
    
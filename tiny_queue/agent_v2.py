from appdirs import user_cache_dir
from sqlitedict import SqliteDict
from filelock import FileLock
from loguru  import logger
import threading
import time
import subprocess
import signal

class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, **kwargs):
        def target(**kwargs):
            try:
                self.process = subprocess.Popen(self.cmd,shell=True,**kwargs)
                self.process.communicate()
            except:
                pass

        thread = threading.Thread(target=target, kwargs=kwargs)
        thread.start()
        return thread


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

def agent_loop(connection):
    logger.info(f"Starting agent")
    while True:
        next_task = get_next_task()
        logger.info(f'Running task "{next_task}"')
        cmd = Command(next_task)
        thread = cmd.run()
        while thread.is_alive():
            time.sleep(1)
            if connection.should_quit(): #check if we need to terminate
                cmd.process.send_signal(signal.SIGINT)
                break
                
            
            # subprocess.check_call(next_task,shell=True)
        
        

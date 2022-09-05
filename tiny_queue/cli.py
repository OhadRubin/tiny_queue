import fire
from .worker import worker_loop
from .writer import write_task        
from appdirs import user_cache_dir
import os
cache_path = user_cache_dir("tiny_cache", "tiny_cache")
os.makedirs(cache_path, exist_ok=True)

def main_loop(cmd:str, task=None):
    if cmd == "worker":
        worker_loop()
    if cmd=="write":
        write_task(task)
        
    else:
        print("Unknown command")
    
def main():
    fire.Fire(main_loop)
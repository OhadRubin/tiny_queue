import fire
from .agent import agent_loop
from .submit import submit_task        
from appdirs import user_cache_dir
import os
cache_path = user_cache_dir("tiny_cache", "tiny_cache")
os.makedirs(cache_path, exist_ok=True)

def main_loop(cmd:str, task=None):
    if cmd == "agent":
        agent_loop()
    if cmd=="submit":
        submit_task(task)
        
    else:
        print("Unknown command")
    
def main():
    fire.Fire(main_loop)
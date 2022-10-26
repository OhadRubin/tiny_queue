import fire
from tiny_queue.agent import agent_loop
from tiny_queue.submit import submit_task        
from tiny_queue.login import redis_login
from appdirs import user_cache_dir
import os
cache_path = user_cache_dir("tiny_cache", "tiny_cache")
os.makedirs(cache_path, exist_ok=True)

def main_loop(cmd:str, task=None):
    if cmd == "agent":
        agent_loop()
    if cmd=="submit":
        submit_task(task)
    if cmd=="clear":
        clear_queue()
    if cmd=="list":
        list_queue()
    if cmd=="login":
        redis_login()
    if cmd=="help":
        print("#TODO help")
    if cmd=="killall":
        killall()
    if cmd=="remove":
        remove_task(task)
        
    else:
        print("Unknown command")
    
def main():
    fire.Fire(main_loop)

if __name__ == '__main__':
    main()
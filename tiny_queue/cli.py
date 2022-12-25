import fire
from tiny_queue.agent import agent_loop
from tiny_queue.submit import submit_task        
from tiny_queue.login import redis_login
from appdirs import user_cache_dir
import os
cache_path = user_cache_dir("tiny_cache", "tiny_cache")
os.makedirs(cache_path, exist_ok=True)

def main_loop(cmd:str, task=None,queue="redis",username=None,password=None,host=None,port=None):
    if cmd == "agent":
        agent_loop(queue)
    elif cmd=="submit":
        submit_task(task,queue)
    elif cmd=="clear":
        clear_queue()
    elif cmd=="list":
        list_queue()
    elif cmd=="login":
        redis_login(username,password,host,port)
    elif cmd=="help":
        print("#TODO help")
    elif cmd=="killall":
        killall()
    elif cmd=="remove":
        remove_task(task)
        
    else:
        print("Unknown command")
    
def main():
    fire.Fire(main_loop)

if __name__ == '__main__':
    main()

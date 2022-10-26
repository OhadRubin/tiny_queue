from appdirs import user_cache_dir
import getpass
import json
from appdirs import user_cache_dir


CACHE_PATH = user_cache_dir("tiny_cache", "tiny_cache")


def get_field(name,default_value):
    value = input(f"Enter {name}, or press enter to use default ({default_value}): ")
    if len(value) == 0:
        return default_value
    return value
    
def redis_login():
    host = get_field("host","redis-14400.c1.us-east1-2.gce.cloud.redislabs.com")
    username = get_field("username","default")
    password = getpass.getpass("Enter the password: ")
    with open(f"{CACHE_PATH}/redis_config.json","w") as f:
        json.dump(dict(host=host,username=username,
                       password=password,
                       port=14400,db=0),f)

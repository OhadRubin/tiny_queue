from appdirs import user_cache_dir
import getpass
import json
from loguru  import logger


DEFAULT_HOST = "redis-14400.c1.us-east1-2.gce.cloud.redislabs.com"
CACHE_PATH = user_cache_dir("tiny_cache", "tiny_cache")


def get_field(name,default_value):
    value = input(f"Enter {name}, or press enter to use default ({default_value}): ")
    if len(value) == 0:
        return default_value
    return value
    
def redis_login(tup=None):
    if tup is None:
        host = get_field("host",DEFAULT_HOST)
        username = get_field("username","default")
        port = int(get_field("port","14400"))
        password = getpass.getpass("Enter the password: ")
        
    else:
        username,password,host,port = tup
        assert password is not None
        username = "default" if username is None
        port = "default" if port is None
        host = DEFAULT_HOST if host is None
    logger.info("Saving config.")
        
    with open(f"{CACHE_PATH}/redis_config.json","w") as f:
        json.dump(dict(host=host,username=username,
                       password=password,
                       port=port,db=0),f)

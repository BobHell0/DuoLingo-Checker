# https://psutil.readthedocs.io/en/latest/#
import psutil
from pprint import pprint

APP_TO_CLOSE = "Notes"
pid = -1

for proc in psutil.process_iter(['pid', 'name', 'username']):
    if proc.info["name"] == APP_TO_CLOSE:
        pprint(proc.info)
        pid = proc.info["pid"]
        proc.terminate()
        

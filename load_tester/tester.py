import requests
import time
import random
import threading

def run():
    while True:
        try:
            requests.get('http://service:5000/flaky')
        except:
            pass

if __name__ == '__main__':
    for _ in range(4):
        thread = threading.Thread(target=run)
        thread.setDaemon(True)
        thread.start()

    while True:
        time.sleep(1)
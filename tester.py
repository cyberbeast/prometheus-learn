import urllib.request
import time
for i in range(2000):
    with urllib.request.urlopen('http://localhost:5000/hello/sandesh') as response:
        print(response.read())
    time.sleep(0.1)
    
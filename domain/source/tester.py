import threading
from threading import Timer
import time

def hello():
    # time.sleep(1.0)
    print("hello, world------------------------------------------------")


# t = Timer(0.1, hello)
# t.start()  # after 3 seconds, "hello, world" will be printed

# print(threading.active_count())
for i in range(100000):
    if threading.active_count() == 1:
        t = Timer(0.25, hello)
        t.start()  # after 3 seconds, "hello, world" will be printed
    print("before hello")
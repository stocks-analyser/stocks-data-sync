import sys

import os
import signal
import time

LAST_SUCCESS_FILE = '/tmp/last_success'
POLL_INTERVAL = 30  # how often your API loop runs
TOUCH_INTERVAL = 30  # how often you want to touch the file

def touch_file(signum, frame):
    """Signal handler: update mtime of LAST_SUCCESS_FILE."""
    now = time.time()
    # ensure the file exists, then update its times
    open(LAST_SUCCESS_FILE, 'a').close()
    os.utime(LAST_SUCCESS_FILE, (now, now))
    print("now: ", now)

def main_loop():
    """Your existing API polling loop."""
    print("hello world")
    print("Python version:", sys.version)
    while True:
    #     try:
    #         resp = requests.get('https://api.example.com/data')
    #         resp.raise_for_status()
    #         data = resp.json()
    #         # … process your data …
    #     except Exception as e:
    #         print("API error:", e)
        time.sleep(POLL_INTERVAL)

if __name__ == '__main__':
    # 1) Install the signal handler:
    signal.signal(signal.SIGALRM, touch_file)
    # 2) Schedule first alarm in TOUCH_INTERVAL, then every TOUCH_INTERVAL:
    signal.setitimer(signal.ITIMER_REAL, TOUCH_INTERVAL, TOUCH_INTERVAL)
    # 3) Ensure file exists immediately:
    open(LAST_SUCCESS_FILE, 'a').close()
    # 4) Enter your main API loop:
    main_loop()

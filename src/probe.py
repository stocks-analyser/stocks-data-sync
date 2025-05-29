# probe.py
import sys
import os
import time

# e.g., check that your main script has written a “last success” timestamp file
stamp_path = '/tmp/last_success'
if not os.path.exists(stamp_path):
    sys.exit(1)
# consider healthy if file updated in last minute
if time.time() - os.path.getmtime(stamp_path) > 60:
    sys.exit(1)
sys.exit(0)
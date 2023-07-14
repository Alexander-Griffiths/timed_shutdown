import datetime
import time
import os

def job():
    os.system("shutdown /s /t 1")

target_hour = 15  # Target hour (6 PM)
target_minute = 7  # Target minute
target_second = 0  # Target second

while True:
    now = datetime.datetime.now()
    target_time = now.replace(hour=target_hour, minute=target_minute, second=target_second, microsecond=0)

    if now >= target_time:
        job()
        break
    
    time_diff = (target_time - now).total_seconds()
    print(f"Time till shutdown -> {time_diff} seconds")
    time.sleep(1)  

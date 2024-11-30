#!/usr/bin/python3 

from datetime import datetime, timedelta
from astral import LocationInfo
from astral.sun import sun
import pytz
import os

def run_script(run_time):
  command = f"echo '/home/fogcat5/youtube-dl/save_video.sh' | at {run_time.strftime('%I:%M %p')}"
  print(command)
  os.system(command)
  

location = LocationInfo("Seacliff", "USA", "America/Los_Angeles", 36.9741, -121.9158)
local_tz = pytz.timezone(location.timezone)

today = datetime.now(local_tz)
s = sun(location.observer, date=today)

sunset_utc = s['sunset']
sunset_local = sunset_utc.astimezone(local_tz)

run_time = sunset_local - timedelta(minutes=15)
if today > run_time:
    print("not scheduling - too late today")
    exit(0)

run_script(run_time)
run_script(sunset_local)

print(f"Task scheduled for {run_time.strftime('%Y-%m-%d %H:%M:%S')}")

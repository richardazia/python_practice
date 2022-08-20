# Experimenting with date and time in python

import calendar
from datetime import datetime
calendar.setfirstweekday(calendar.MONDAY)
import time

time_test = time.localtime()
print(time_test)
hour = time_test.tm_hour
min = time_test.tm_min
secs = time_test.tm_sec
month_end = time_test.tm_mon
if month_end == 1:
  print('1st')
elif month_end ==2:
  print("Second")
elif month_end == 3:
  print("third")
else:
  print("th")

print(f"Month end: {month_end}")

print(f"For a brief moment the time was {hour}:{min}:{secs}")
print
day = 6
temp = 19


week_day = calendar.weekday(2022, 8, 20)
print(f"The day of the week is: {week_day}")

# Name of the week day
if day == 0:
    day_name = "Monday"
elif day == 1:
    day_name = 'Tuesday'
elif day == 2:
    day_name = 'Wednesday'
elif day == 3:
    day_name = 'Thursday'
elif day == 4:
    day_name = 'Friday'
elif day == 5:
    day_name = 'Saturday'
else:
    day_name = 'Sunday'

# Name of the Month

if month_end == 1:
  month_name = "January"
elif month_end == 2:
  month_name = "February"
elif month_end == 3:
  month_name = "March"
elif month_end == 4:
  month_name = "April"
elif month_end == 5:
  month_name = "May"
elif month_end == 6:
  month_name = "June"
elif month_end == 7:
  month_name = "July"
elif month_end == 8:
  month_name = "August"
elif month_end == 9:
  month_name = "September"
elif month_end == 10:
  month_name = "Octobre"
elif month_end == 11:
  month_name = "Novembre"
else:
  month_name = "Decembre"

print(f"Today is day: {day}, {day_name}, in the month of {month_name} and the outside air temperature is {temp}°c")

# Experiment with python-weather

import python_weather
import asyncio
import os

async def getweather():
  # declare client, format default to metric.
  async with python_weather.Client(format=python_weather.METRIC) as client:
    
    # Fetch weather from Lausanne
    weather = await client.get("Lausanne")

    lausanne_temp = weather.current.temperature
    lausanne_desc = weather.current.description
    # local_time = weather.current.local_time
    # local_uv = weather.current.uv_index

    print(lausanne_temp)
    # print(f"The current time is {local_time} and the UV index is of {local_uv}")
    print(f"Today is day: {day}, {day_name}, in the month of {month_name} and the outside air temperature is {lausanne_temp}°c.\nCurrent weather: {lausanne_desc}")

    # see the weather for a few days
    for forecast in weather.forecasts:
      print(forecast.date, forecast.astronomy)

      #Hourly
      for hourly in forecast.hourly:
        print(f' --> {hourly!r}')

if __name__ == "__main__":
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
  if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  asyncio.run(getweather())


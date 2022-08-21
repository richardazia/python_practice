# # Experimenting with date and time in python

# import calendar
# from datetime import datetime
# calendar.setfirstweekday(calendar.MONDAY)
# import time
# import random
# import art

# time_test = time.localtime()
# print(time_test)
# hour = time_test.tm_hour
# min = time_test.tm_min
# secs = time_test.tm_sec
# month_end = time_test.tm_mon
# if month_end == 1:
#   print('1st')
# elif month_end ==2:
#   print("Second")
# elif month_end == 3:
#   print("third")
# else:
#   print("th")

# print(f"Month end: {month_end}")

# print(f"For a brief moment the time was {hour}:{min}:{secs}")
# print
# day = 6
# temp = 19


# week_day = calendar.weekday(2022, 8, 20)
# print(f"The day of the week is: {week_day}")

# # Name of the week day
# if day == 0:
#     day_name = "Monday"
# elif day == 1:
#     day_name = 'Tuesday'
# elif day == 2:
#     day_name = 'Wednesday'
# elif day == 3:
#     day_name = 'Thursday'
# elif day == 4:
#     day_name = 'Friday'
# elif day == 5:
#     day_name = 'Saturday'
# else:
#     day_name = 'Sunday'

# # Name of the Month

# if month_end == 1:
#   month_name = "January"
# elif month_end == 2:
#   month_name = "February"
# elif month_end == 3:
#   month_name = "March"
# elif month_end == 4:
#   month_name = "April"
# elif month_end == 5:
#   month_name = "May"
# elif month_end == 6:
#   month_name = "June"
# elif month_end == 7:
#   month_name = "July"
# elif month_end == 8:
#   month_name = "August"
# elif month_end == 9:
#   month_name = "September"
# elif month_end == 10:
#   month_name = "Octobre"
# elif month_end == 11:
#   month_name = "Novembre"
# else:
#   month_name = "Decembre"

# print(f"Today is day: {day}, {day_name}, in the month of {month_name} and the outside air temperature is {temp}°c")

# # Experiment with python-weather

# import python_weather
# import asyncio
# import os

# async def getweather():
#   # declare client, format default to metric.
#   async with python_weather.Client(format=python_weather.METRIC) as client:
    
#     # Fetch weather from Lausanne
#     weather = await client.get("Lausanne")

#     lausanne_temp = weather.current.temperature
#     lausanne_desc = weather.current.description
#     # local_time = weather.current.local_time
#     # local_uv = weather.current.uv_index

#     print(lausanne_temp)
#     # print(f"The current time is {local_time} and the UV index is of {local_uv}")
#     print(f"Today is day: {day}, {day_name}, in the month of {month_name} and the outside air temperature is {lausanne_temp}°c.\nCurrent weather: {lausanne_desc}")

#     # see the weather for a few days
#     for forecast in weather.forecasts:
#       print(forecast.date, forecast.astronomy)

#       #Hourly
#       for hourly in forecast.hourly:
#         print(f' --> {hourly!r}')

# if __name__ == "__main__":
#   # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
#   # for more details
#   if os.name == "nt":
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

#   asyncio.run(getweather())

# # Playing with booleans

# weekend = False

# if weekend: 
#   print("48 hours of freedom from the world")
# else: 
#   print("Time to take the week seriously")

# age = 19

# if age <= 17:
#   print("Enjoy being a child")
# else:
#   print("Be a responsible adult. ")

# print(random.randrange(10, 50, 3))

# # Magic eight ball
# Art=art.text2art("Magic Eight Ball") # Return ASCII text (default font) and default chr_ignore=True 
# print(Art)
# eight_ball = random.randint(1, 8)
# print("Ask the Magic eight ball a question and see what it thinks?")
# question = input("-->")
# if eight_ball <= 2:
#   print("Yep")
# elif eight_ball == 3 or eight_ball == 4:
#   print("Maybe")
# elif eight_ball >= 5 and eight_ball <= 6:
#   print("Roll the ball again")
# else:
#   print("Nope")

# ctrl § to mark as comment in windows

#######################################

import random
import art

lucky_number = random.randint(1,100)
if lucky_number == 44:
  print("The odds of you having a great day are one in 1/100. Congrats on getting that one right")
else:
  print(f"What do you want to do with your unlucky numbers? This time you got  {lucky_number}." )

Art=art.text2art("Random ride") # Return ASCII text (default font) and default chr_ignore=True 
print(Art)

#### Lists

villages = ["La Rippe", "Bursins", "Duiller", "Vich", "Gland"]

print(villages)
print(villages[0])
villages.append("Trelex")
villages.append("Borex")
villages.append("Le Pont")
villages.append("Muids")
villages.append("Muids")
villages.append("Muids")
villages.append("Grandson")
print(villages)

print(len(villages))
number_of_villages = villages.count

print(number_of_villages("Muids"))

villages.insert(6, "Champoussin")
villages.insert(3, "Gland")
print(villages)
# del(villages[6])
# del(villages[2])
# del(villages[0])
# del(villages[9])
# del(villages[9])
# del(villages[6])
print(villages)

for mistakes in range(10):
  print(str(mistakes) + " " + "mistakes made")

i = 1
village_title=art.text2art("Village List") # Return ASCII text (default font) and default chr_ignore=True 
print(village_title)
for village in villages:
  print(f"{i}: {village}")
  i += 1
print("End of list")

quarantaine = art.text2art("Quarantine count down")
print(quarantaine)
multiple_of_two = 2
for multiple_of_two in range(2, 42, 2):
  print(multiple_of_two)

#### Dictionaries

birds = {"Fred" : "duck", "Gilbert": "crane", "John": "Spoonbill", "Anna": "Pelican", "Ross" : "Albatros", "Bill": "goat"}

print(birds)

print(f'Ross, the {birds["Ross"]}')
print(f'Anna is a {birds["Anna"]}')
print(len(birds))
del(birds["Bill"])
print(len(birds))

ducks_given = {1: True, 2: False, 3: False, 4: True, 5: True, 6: True, 7: False, 8: False}
print(f"Number of ducks given: {len(ducks_given)}")
print(ducks_given)
print(ducks_given.keys())
del(ducks_given[1])
del(ducks_given[6])
print(ducks_given.values())

# Text taken from Magna carta entry, written in English: https://en.wikipedia.org/wiki/Magna_Carta
text = """"
Magna Carta Libertatum (Medieval Latin for "Great Charter of Freedoms"), commonly called Magna Carta (also Magna Charta; "Great Charter"),[a] is a royal charter[4][5] of rights agreed to by King John of England at Runnymede, near Windsor, on 15 June 1215.[b] First drafted by Archbishop of Canterbury, Cardinal Stephen Langton, to make peace between the unpopular king and a group of rebel barons, it promised the protection of church rights, protection for the barons from illegal imprisonment, access to swift justice, and limitations on feudal payments to the Crown, to be implemented through a council of 25 barons. Neither side stood behind their commitments, and the charter was annulled by Pope Innocent III, leading to the First Barons' War.

After John's death, the regency government of his young son, Henry III, reissued the document in 1216, stripped of some of its more radical content, in an unsuccessful bid to build political support for their cause. At the end of the war in 1217, it formed part of the peace treaty agreed at Lambeth, where the document acquired the name "Magna Carta", to distinguish it from the smaller Charter of the Forest which was issued at the same time. Short of funds, Henry reissued the charter again in 1225 in exchange for a grant of new taxes. His son, Edward I, repeated the exercise in 1297, this time confirming it as part of England's statute law. The charter became part of English political life and was typically renewed by each monarch in turn, although as time went by and the fledgling Parliament of England passed new laws, it lost some of its practical significance.

At the end of the 16th century, there was an upsurge in interest in Magna Carta. Lawyers and historians at the time believed that there was an ancient English constitution, going back to the days of the Anglo-Saxons, that protected individual English freedoms. They argued that the Norman invasion of 1066 had overthrown these rights, and that Magna Carta had been a popular attempt to restore them, making the charter an essential foundation for the contemporary powers of Parliament and legal principles such as habeas corpus. Although this historical account was badly flawed, jurists such as Sir Edward Coke used Magna Carta extensively in the early 17th century, arguing against the divine right of kings. Both James I and his son Charles I attempted to suppress the discussion of Magna Carta. The political myth of Magna Carta and its protection of ancient personal liberties persisted after the Glorious Revolution of 1688 until well into the 19th century. It influenced the early American colonists in the Thirteen Colonies and the formation of the United States Constitution, which became the supreme law of the land in the new republic of the United States.[c] Research by Victorian historians showed that the original 1215 charter had concerned the medieval relationship between the monarch and the barons, rather than the rights of ordinary people, but the charter remained a powerful, iconic document, even after almost all of its content was repealed from the statute books in the 19th and 20th centuries. Three clauses (1, 9, and 29) remain in force in England and Wales.

Magna Carta still forms an important symbol of liberty today, often cited by politicians and campaigners, and is held in great respect by the British and American legal communities, Lord Denning describing it as "the greatest constitutional document of all times—the foundation of the freedom of the individual against the arbitrary authority of the despot".[6] In the 21st century, four exemplifications of the original 1215 charter remain in existence, two at the British Library, one at Lincoln Castle and one at Salisbury Cathedral. There are also a handful of the subsequent charters in public and private ownership, including copies of the 1297 charter in both the United States and Australia. Although scholars refer to the 63 numbered "clauses" of Magna Carta, this is a modern system of numbering, introduced by Sir William Blackstone in 1759; the original charter formed a single, long unbroken text. The four original 1215 charters were displayed together at the British Library for one day, 3 February 2015, to mark the 800th anniversary of Magna Carta. 
"""

text_old = """"
The quick brown fox jumped over the lazy dog and then went for a jog around the village. He then went to start a fight with a mite, before jumping down to the sea shore. 
From the sea shore he walked to a cave and went into the cave. The cave was filled with frogs, ducks and monkeys. This was a very strange cave. 
They were all sheltering from that day's rain, and when it would stop, they would retreat and rest. 
Now to see if the word count goes up. 
What did the goat say to the other goat? Did the goat run around the forest? Did the forest wrap around the goat? 
How many monkeys does it change to change a light bulb? 
How many monkeys are jumping on the bed. 
"""
# print(text)
# print(text.split())
print(len(text.split()))

word_count = {}

for word in text.lower().split():
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

print(word_count)


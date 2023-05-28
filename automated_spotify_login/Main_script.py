from datetime import date
from datetime import datetime
from time import time 
from spotify_bot import spotifylogbot
from emails import startup


timenow=datetime.now()
timereport=timenow.strftime("%H:%M:%S")

print("script started runninng on:",date.today(),"time: ",timereport)


today=date.today()

schedule_time="12:30:00"

set_weekday=6
if set_weekday==0:
    scheduled_day=="Monday"
elif set_weekday==1:
    scheduled_day="Tuesday"
elif set_weekday==2:
    scheduled_day="Wednesday"
elif set_weekday==3:
    scheduled_day="Thursday"
elif set_weekday==4:
    scheduled_day="Friday"
elif set_weekday==5:
    scheduled_day="Saturday"
elif set_weekday==6:
    scheduled_day="Sunday"

print("scheduled for",scheduled_day,"at:",schedule_time,"every week")

startup()

while True:
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    if current_time==schedule_time and today.weekday()==set_weekday:
        print("It's Time. running your script now")
        verify=spotifylogbot()
        if verify==True:
            print("Run finished successfully on:",date.today(),"at:",datetime.now())
            print("Running again next week at same time")
        elif verify==False:
            print("Running unsuccessful. Running again")
            verify=spotifylogbot()


import slack
import datetime
import time
import os

SLACK_TOKEN = os.environ["HOUSE_SLACK_KEY"]
client = slack.WebClient(token=SLACK_TOKEN)

# names = ["Eshaan", "Nathan", "Rajen", "Aditya", "Michael", "Patrick", "Will"]
schedule = ["U03TCU4KTCZ", "U03UF82K334", "U03UE9Q3BNH", "U03U1NM61DM", "U03UVDH5FGR", "U03U8KHH9E2", "U03V63NLY0G"]

def get_who_dishes(t, schedule):
    weekday = t.weekday()
    return schedule[weekday - 1]

def get_who_trash(t, schedule):
    weekday = t.weekday()
    return schedule[weekday % 7]

# hours=18 -> 6pm
t = datetime.datetime(year=2022, month=8, day=24, hour=18, tzinfo=datetime.timezone(datetime.timedelta(hours=-8)))
for _ in range(120):
    unix_time = time.mktime(t.timetuple())
    client.chat_scheduleMessage(channel='#chores', text=f"Do the dishes <@{get_who_dishes(t, schedule)}>", post_at=unix_time)
    client.chat_scheduleMessage(channel='#chores', text=f"Take out the trash <@{get_who_trash(t, schedule)}>", post_at=unix_time)
    t += datetime.timedelta(days=1)
print("Done")
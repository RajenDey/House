import datetime
import time
import os
from enum import Enum
import slack
from who import Who

SLACK_TOKEN = os.environ["HOUSE_SLACK_KEY"]
client = slack.WebClient(token=SLACK_TOKEN)

class Stepsize(Enum):
    DAY = 1
    WEEK = 2
    FORTNITE = 3

class Chores:
    def __init__(self, start_time: datetime.datetime, message: str, stepsize: Stepsize, who: Who):
        self.t = start_time
        self.message = message
        self.stepsize = stepsize
        self.who = who
    
    def schedule_messages(self, timesteps: int):
        for _ in range(timesteps):
            print(f"scheduling message for {self.t}")
            unix_time = time.mktime(self.t.timetuple())
            client.chat_scheduleMessage(channel='#chores', text=f"{self.message} <@{self.who.get_who(self.t)}>", post_at=unix_time)
            self.step()
    
    def step(self):
        if self.stepsize == Stepsize.DAY:
            self.t += datetime.timedelta(days=1)
        elif self.stepsize == Stepsize.WEEK:
            self.t += datetime.timedelta(weeks=1)
        elif self.stepsize == Stepsize.FORTNITE:
            self.t += datetime.timedelta(weeks=2)

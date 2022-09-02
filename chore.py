from datetime import datetime
from time import mktime
from os import environ
from slack import WebClient
from who import Who
from stepsize import Stepsize

SLACK_TOKEN = environ["HOUSE_SLACK_KEY"]
client = WebClient(token=SLACK_TOKEN)

class Chore:
    def __init__(self, start_time: datetime, message: str, stepsize: Stepsize, who: Who):
        self.t = start_time
        self.message = message
        self.stepsize = stepsize
        self.who = who
    
    def schedule_messages(self, timesteps: int):
        for _ in range(timesteps):
            print(f"scheduling message for {self.t}")
            unix_time = mktime(self.t.timetuple())
            client.chat_scheduleMessage(channel='#chores', text=f"{self.message} <@{self.who.get_who(self.t)}>", post_at=unix_time)
            self.t += self.stepsize.timedelta()

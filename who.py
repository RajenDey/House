from datetime import datetime
from constants import SCHEDULE

class Who:
    START_TIME = datetime(year=2022, month=8, day=30, hour=6, minute=41)
    def get_who(self, t: datetime):
        pass

class WhoDishes(Who):
    def get_who(self, t: datetime):
        weekday = t.weekday()
        return SCHEDULE[weekday - 1]

class WhoTrash(Who):
    def get_who(self, t: datetime):
        weekday = t.weekday()
        return SCHEDULE[weekday % len(SCHEDULE)]

class WhoDumpster(Who):
    def get_who(self, t: datetime):
        diff = t - self.START_TIME
        weeks = diff.days // 7
        return SCHEDULE[weeks % len(SCHEDULE)]

class WhoCleaning(Who):
    def get_who(self, t: datetime):
        diff = t - self.START_TIME
        weeks = diff.days // 7
        return SCHEDULE[(weeks + 1) % len(SCHEDULE)]

class WhoRefrigerator(Who):
    def get_who(self, t: datetime):
        diff = t - self.START_TIME
        fortnites = diff.days // 14
        return SCHEDULE[(fortnites + 1) % len(SCHEDULE)]
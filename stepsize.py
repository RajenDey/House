from enum import Enum
from datetime import timedelta

class Stepsize(Enum):
    DAY = 1
    WEEK = 2
    FORTNITE = 3

    def timedelta(self):
        if self == self.DAY:
            return timedelta(days=1)
        if self == self.WEEK:
            return timedelta(weeks=1)
        if self == self.FORTNITE:
            return timedelta(weeks=2)

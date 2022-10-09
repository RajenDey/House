from datetime import datetime
from os import environ
from slack import WebClient
from chore import Chore
from stepsize import Stepsize
from who import *
from constants import DAY_TIMESTEPS, WEEK_TIMESTEPS, FORTNITE_TIMESTEPS

SLACK_TOKEN = environ["HOUSE_SLACK_KEY"]
client = WebClient(token=SLACK_TOKEN)

# update these when re-run
daily_9am = datetime(year=2022, month=10, day=9, hour=9)
monday_9am = datetime(year=2022, month=10, day=10, hour=9)
tuesday_9am = datetime(year=2022, month=10, day=11, hour=9)
saturday_9am = datetime(year=2022, month=10, day=15, hour=9)

trash = Chore(client, daily_9am, "Take out the trash", Stepsize.DAY, WhoTrash())
dumpster_out = Chore(client, monday_9am, "Take out the dumpster", Stepsize.WEEK, WhoDumpster())
dumpster_in = Chore(client, tuesday_9am, "Bring the dumpster in", Stepsize.WEEK, WhoDumpster())
dishes = Chore(client, daily_9am, "Do the dishes", Stepsize.DAY, WhoDishes())
cleaning = Chore(client, saturday_9am, "Mop the floors and clean the surfaces", Stepsize.WEEK, WhoCleaning())
refrigerator = Chore(client, saturday_9am, "Clean out the refrigerators", Stepsize.FORTNITE, WhoRefrigerator())

trash.schedule_messages(DAY_TIMESTEPS)
dumpster_out.schedule_messages(WEEK_TIMESTEPS)
dumpster_in.schedule_messages(WEEK_TIMESTEPS)
dishes.schedule_messages(DAY_TIMESTEPS)
cleaning.schedule_messages(WEEK_TIMESTEPS)
# refrigerator.schedule_messages(FORTNITE_TIMESTEPS)

from datetime import datetime
from chore import Chore
from stepsize import Stepsize
from who import *
from constants import DAY_TIMESTEPS, WEEK_TIMESTEPS, FORTNITE_TIMESTEPS

# update these when re-run
daily_9am = datetime(year=2022, month=9, day=2, hour=9)
wednesday_9am = datetime(year=2022, month=9, day=7, hour=9)
saturday_9am = datetime(year=2022, month=9, day=3, hour=9)

trash = Chore(daily_9am, "Take out the trash", Stepsize.DAY, WhoTrash())
dumpster = Chore(wednesday_9am, "Take out the dumpster", Stepsize.WEEK, WhoDumpster())
dishes = Chore(daily_9am, "Do the dishes", Stepsize.DAY, WhoDishes())
cleaning = Chore(saturday_9am, "Mop the floors and clean the surfaces", Stepsize.WEEK, WhoCleaning())
refrigerator = Chore(saturday_9am, "Clean out the refrigerators", Stepsize.FORTNITE, WhoRefrigerator())

trash.schedule_messages(DAY_TIMESTEPS)
dumpster.schedule_messages(WEEK_TIMESTEPS)
dishes.schedule_messages(DAY_TIMESTEPS)
cleaning.schedule_messages(WEEK_TIMESTEPS)
# refrigerator.schedule_messages(FORTNITE_TIMESTEPS)

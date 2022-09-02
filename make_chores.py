import chores
from datetime import datetime
from constants import DAY_TIMESTEPS, WEEK_TIMESTEPS, FORTNITE_TIMESTEPS
import who

# update these when re-run
daily_9am = datetime(year=2022, month=9, day=2, hour=9)
wednesday_9am = datetime(year=2022, month=9, day=7, hour=9)
saturday_9am = datetime(year=2022, month=9, day=3, hour=9)

trash = chores.Chores(daily_9am, "Take out the trash", chores.Stepsize.DAY, who.WhoTrash())
dumpster = chores.Chores(wednesday_9am, "Take out the dumpster", chores.Stepsize.WEEK, who.WhoDumpster())
dishes = chores.Chores(daily_9am, "Do the dishes", chores.Stepsize.DAY, who.WhoDishes())
cleaning = chores.Chores(saturday_9am, "Mop the floors and clean the surfaces", chores.Stepsize.WEEK, who.WhoCleaning())
refrigerator = chores.Chores(saturday_9am, "Clean out the refrigerators", chores.Stepsize.FORTNITE, who.WhoRefrigerator())

trash.schedule_messages(DAY_TIMESTEPS)
dumpster.schedule_messages(WEEK_TIMESTEPS)
dishes.schedule_messages(DAY_TIMESTEPS)
cleaning.schedule_messages(WEEK_TIMESTEPS)
# refrigerator.schedule_messages(FORTNITE_TIMESTEPS)

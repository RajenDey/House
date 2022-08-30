import chores
from datetime import datetime
from constants import DAY_TIMESTEPS, FORTNITE_TIMESTEPS, WEEK_TIMESTEPS
import who

day_t = datetime(year=2022, month=8, day=30, hour=9)
week_t = datetime(year=2022, month=9, day=3, hour=9)
fortnite_t = week_t

trash = chores.Chores(day_t, "Take out the trash", chores.Stepsize.DAY, who.WhoTrash())
dumpster = chores.Chores(week_t, "Take out the dumpster", chores.Stepsize.WEEK, who.WhoDumpster())
dishes = chores.Chores(day_t, "Do the dishes", chores.Stepsize.DAY, who.WhoDishes())
cleaning = chores.Chores(week_t, "Mop the floors and clean the surfaces", chores.Stepsize.WEEK, who.WhoCleaning())
refrigerator = chores.Chores(fortnite_t, "Clean out the refrigerators", chores.Stepsize.FORTNITE, who.WhoRefrigerator())

trash.schedule_messages(DAY_TIMESTEPS)
dumpster.schedule_messages(WEEK_TIMESTEPS)
dishes.schedule_messages(DAY_TIMESTEPS)
cleaning.schedule_messages(WEEK_TIMESTEPS)
refrigerator.schedule_messages(FORTNITE_TIMESTEPS)

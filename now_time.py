import datetime as dt
import time as tm
now = dt.datetime.fromtimestamp(tm.time())
todaydate = dt.datetime.today()
delta = dt.timedelta(days=0)
print(f'the date and time is: {todaydate-delta}')

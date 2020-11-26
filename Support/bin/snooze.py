#!/usr/local/bin/python3
####!/usr/bin/env python3

import sys
import datetime
import pytz

WEEKDAYS = "mon", "tue", "wed", "thu", "fri", "sat", "sun"
TIMESPEC = "d", "w", "m"


def timespec2days(spec):
  unit = spec[-1]
  amount = int(spec[0:len(spec) - 1])
  
  if unit == "d": return amount
  elif unit == "w": return amount * 7
  elif unit == "m": return amount * 30
  else: 
    raise ValueError("Invalid unit in timespec: '" + unit + "'")


dt = datetime.datetime.today()
dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)

# standardize user input
x = sys.argv[1].lower().strip()

# check if weekday was entered
if x in WEEKDAYS: 
  twd = WEEKDAYS.index(x)  # target weekday
  delta = twd - dt.weekday()  
  if delta <= 0: delta += 7   # days until target wd
  dt = dt + datetime.timedelta(days=delta)
  
# "tom" = tomorrow
elif x == "tom": # tomorrow
  delta = 1
  dt = dt + datetime.timedelta(days=delta)

# specified "d" "m" or "w"?
elif x[-1] in TIMESPEC:
  delta = timespec2days(x)
  dt = dt + datetime.timedelta(days=delta)

# target date yyyy-mm-dd
else:
  try:
    dt = datetime.datetime.strptime(x, "%Y-%m-%d")
    dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
  except:
    ValueError("Invalid snooze time format: '" + x + "'")

until = dt.strftime("%A, %b %-d %Y")
dt = pytz.timezone('UTC').localize(dt)
dts = dt.strftime("%Y-%m-%d")

out = '''
{ actions = (
	{
		type = "changeHeaders";
		headers = { 
		  "x-snooze" = "%s"; 
		};
	},
  {
    type = "notify";
    formatString = "Snoozed until %s";
  },
  {
    type    = "changeFlags";
    enable  = ( "\\Seen", "\\$NotJunk", "$snoozed");
    disable = ( "\\$Junk", "\\Junk");
  },
); }
''' % (dts, until)


print (out)


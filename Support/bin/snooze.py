#!/usr/local/bin/python3

import sys
import datetime
import pytz
from Support.bin.snooze_helpers import snooze2days, snooze2targetdate

UNSNOOZE_OUTPUT = '''
{ actions = (
    {
        type = "changeHeaders";
        headers = { 
          "x-snooze" = ""; 
        };
    },
  {
    type = "notify";
    formatString = "Message unsnoozed";
  },
  {
    type    = "changeFlags";
    disable = ( "$snoozed");
  },
); }
'''

# standardize user input
x = sys.argv[1].lower().strip()

if x == "xx":
    print(UNSNOOZE_OUTPUT)
else:
    days = snooze2days(x)
    dt = datetime.datetime.today()

    if days > 0:
        dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
        dt = dt + datetime.timedelta(days)
    else:
        dt = snooze2targetdate(x)  # may raise error

    until = dt.strftime("%A, %b %-d %Y")
    dt = pytz.timezone('UTC').localize(dt)
    dts = dt.strftime("%Y-%m-%d")

    # debug
    # print (days)
    # print (dts)

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

    print(out)

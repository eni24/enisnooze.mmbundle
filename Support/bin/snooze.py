#!/usr/bin/env python3

import sys
import pytz
from snooze_helpers import parse_input

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

    dt = parse_input(x)

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

#!/usr/local/bin/python3
####!/usr/bin/env python3

import sys

out = '''
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
print (out)


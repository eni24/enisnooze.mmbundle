#!/usr/bin/env python3

import datetime

WEEKDAYS = "mon", "tue", "wed", "thu", "fri", "sat", "sun"
TIMESPEC = "d", "w", "m"


def timespec2days(spec):
    if spec is None:
        raise ValueError("Invalid snooze time format: <None>")

    unit = spec[-1]
    amount = int(spec[0:len(spec) - 1])

    if unit == "d":
        return amount
    elif unit == "w":
        return amount * 7
    elif unit == "m":
        return amount * 30

    raise ValueError("Invalid unit in timespec: '" + unit + "'")


def snooze2targetdate(x):
    # target date yyyy-mm-dd
    if x is None:
        raise ValueError("Invalid snooze time format: <None>")

    try:
        dt = datetime.datetime.strptime(x, "%Y-%m-%d")
        return dt.replace(hour=0, minute=0, second=0, microsecond=0)
    except ValueError:
        raise ValueError("Invalid snooze time format: '" + x + "'")


# in: snooze input (e.g. 1d, 2d, 5w, 1m, tom, mon, wed, ...)
# out: days to snooze as integer 
# returns value < 0 if no delta could be calculated
def snooze2days(x):
    # too short -> reject
    if len(x) < 1:
        return -1

    dt = datetime.datetime.today()
    # dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)

    # check if weekday was entered
    if x in WEEKDAYS:
        twd = WEEKDAYS.index(x)  # target weekday
        delta = twd - dt.weekday()
        if delta <= 0:
            delta += 7  # days until target wd
        return delta

    # "tom" = tomorrow
    if x == "tom":
        return 1

    # specified "d" "m" or "w"?
    if x[-1] in TIMESPEC:
        return timespec2days(x)

    # if all fails: return -1
    return -1

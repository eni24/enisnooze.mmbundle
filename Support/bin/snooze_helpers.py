#!/usr/bin/env python3

import datetime

WEEKDAYS = "mon", "tue", "wed", "thu", "fri", "sat", "sun"


def add_months(dt: datetime.datetime, months_to_add: int):
    y = dt.year + ((dt.month + months_to_add) // 12)
    m = (dt.month + months_to_add) % 12
    d = dt.day
    dadd = 0

    # handle end of february
    if m == 2 and d >= 30:
        m, d = 3, 1
    elif m == 2 and d == 29:
        d, dadd = 28, 1
    elif d == 31:
        d, dadd = 30, 1

    result = dt.replace(day=d, month=m, year=y) + datetime.timedelta(dadd)
    return result


def timespec2targetdate(spec, todays_date):
    if spec is None:
        raise ValueError("Invalid snooze time format: <None>")

    if spec in WEEKDAYS:
        twd = WEEKDAYS.index(spec)  # target weekday
        delta = twd - todays_date.weekday()
        if delta <= 0:
            delta += 7  # days until target wd
        return todays_date + datetime.timedelta(delta)

    if spec == "tom":
        return todays_date + datetime.timedelta(1)

    # parse as timespec <n><unit>, e.g. 2d, 5w, 3m
    unit = spec[-1]
    amount = int(spec[0:len(spec) - 1])

    if amount < 0:
        raise ValueError("Nagative value in timespec: '" + spec + "'")

    if unit == "d":
        return todays_date + datetime.timedelta(amount)

    if unit == "w":
        return todays_date + datetime.timedelta(amount * 7)

    if unit == "m":
        return add_months(todays_date, amount)

    raise ValueError("Invalid unit in timespec: '" + unit + "'")


# Parse snooze-String using Standard-Formats
def snooze2targetdate(x, todays_date):

    # try first format
    try:
        return snooze2targetdate_with_format(x, "%Y-%m-%d")
    except (ValueError):
        pass

    # try next format
    try:
        return snooze2targetdate_with_format(x, "%d.%m.%Y")
    except (ValueError):
        pass

    # try next format
    # and let exception fly
    dt = snooze2targetdate_with_format(x, "%d.%m.")
    dt = dt.replace(year=todays_date.year)
    if todays_date >= dt:
        dt = dt.replace(year=todays_date.year + 1)

    return dt


# Parse snooze-String using Standard-Formats and provided date-format
def snooze2targetdate_with_format(x, frmt):
    # target date yyyy-mm-dd
    if x is None:
        raise ValueError("Invalid snooze time format: <None>")

    try:
        dt = datetime.datetime.strptime(x, frmt)
        return dt.replace(hour=0, minute=0, second=0, microsecond=0)
    except ValueError:
        raise ValueError("Invalid snooze time format: '" + x + "'")


def parse_input(x, todays_date=datetime.datetime.today()):

    # special cases
    if x is None:
        raise ValueError("Invalid Input: <None>")
    elif len(x) == 0:
        raise ValueError("Invalid Input with length 0")
    elif x == "ff":
        return datetime.datetime.strptime("3000-01-01", "%Y-%m-%d")

    try:
        # parse as spec (2d, 1m, 3w, ...)
        dt = timespec2targetdate(x, todays_date)
    except(ValueError):
        # parse as date
        dt = snooze2targetdate(x, todays_date)  # may raise error

    return dt

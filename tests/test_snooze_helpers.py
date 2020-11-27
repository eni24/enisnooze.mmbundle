import pytest
from Support.bin.snooze_helpers import snooze2days, snooze2targetdate

@pytest.mark.parametrize("x, y",  [
    ("2d", 2),
    ("5d", 5),
    ("1d", 1),
])
def test_timespec2days_days(x, y):
    assert snooze2days(x) == int(y)


@pytest.mark.parametrize("x,y",  [
    ("1w", 7),
    ("2w", 14),
    ("10w", 70),
])
def test_timespec2days_weeks(x, y):
    assert snooze2days(x) == y


@pytest.mark.parametrize("x,y",  [
    ("1m", 30),
    ("2m", 60),
    ("5m", 150),
])
def test_timespec2days_months(x, y):
    assert snooze2days(x) == y

def test_timespec2days_invalid():
    assert snooze2days("-1m") < 0
    assert snooze2days("xyx") < 0
    assert snooze2days("3x") < 0
    assert snooze2days("") < 0
    assert snooze2days("27l") < 0

@pytest.mark.parametrize("ds", [
    ("1900-01-02"),
    ("2999-12-31"),
    ("2020-02-29"),
    ("1000-12-24"),
])
def test_dateparsing(ds):
    date = snooze2targetdate(ds)
    assert date is not None
    assert date.strftime("%Y-%m-%d") == ds

@pytest.mark.parametrize("ds", [
    ("1900-00-01"),
    ("2050-13-01"),
    ("2050-01-00"),
    ("2050-01-32"),
    ("2050-xy-01"),
    ("2050-01-dd"),
    ("12-01-01"),
    ("1-1-1"),
    ("a"),
    ("1"),
    (""),
    (None),
])
def test_dateparsing_invalid(ds):
    with pytest.raises(ValueError):
        snooze2targetdate(ds)


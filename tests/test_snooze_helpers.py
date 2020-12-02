import pytest
from Support.bin.snooze_helpers import snooze2days, parse_input
import datetime


@pytest.mark.parametrize("ds_today,x,ds_result",  [
    ("2020-06-01", "2d", "2020-06-03"),
    ("2020-06-01", "5d", "2020-06-06"),
    ("2020-06-01", "1d", "2020-06-02"),
    ("2012-12-31", "1d", "2013-01-01"),
])
def test_snooze_days(ds_today, x, ds_result):
    today = datetime.datetime.strptime(ds_today, "%Y-%m-%d")
    snoozedate = parse_input(x, today)
    assert  snoozedate.strftime("%Y-%m-%d") == ds_result


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
def test_dateparsing_ansi(ds):
    date = parse_input(ds)
    assert date is not None
    assert date.strftime("%Y-%m-%d") == ds


@pytest.mark.parametrize("ds,result", [
    ("2.1.1900", "02.01.1900"),
    ("02.1.1900", "02.01.1900"),
    ("2.01.1900", "02.01.1900"),
    ("2.1.1900", "02.01.1900"),
    ("31.12.2999", "31.12.2999"),
    ("29.2.2020", "29.02.2020"),
    ("24.12.1000", "24.12.1000"),
])
def test_dateparsing_dmy(ds, result):
    date = parse_input(ds)
    assert date is not None
    assert date.strftime("%d.%m.%Y") == result


@pytest.mark.parametrize("ds_today,ds,ds_result", [
    ("2.12.2020", "24.12.", "24.12.2020"),
    ("1.1.2030", "2.1.", "02.01.2030"),
    ("2.1.2030", "1.1.", "01.01.2031"),
    ("1.1.2030", "1.1.", "01.01.2031"),
    ("2.12.2020", "02.1.", "02.01.2021"),
    ("2.12.2020", "2.01.", "02.01.2021"),
    ("2.12.2020", "2.1.", "02.01.2021"),
    ("2.12.2020", "31.12.", "31.12.2020"),
    ("2.1.2024", "28.2.", "28.02.2024"),
    ("2.12.2020", "24.12.", "24.12.2020"),
])
def test_dateparsing_dm_without_year(ds_today, ds, ds_result):
    today = datetime.datetime.strptime(ds_today, "%d.%m.%Y")
    snoozedate = parse_input(ds, today)

    assert snoozedate is not None
    assert snoozedate.strftime("%d.%m.%Y") == ds_result


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
])
def test_dateparsing_invalid(ds):
    with pytest.raises(ValueError):
        parse_input(ds)


def test_unspecified_snooze():
    snoozedate = parse_input("ff")

    assert snoozedate is not None
    assert snoozedate.strftime("%Y-%m-%d") == "1900-01-01"


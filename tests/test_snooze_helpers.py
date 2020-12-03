import pytest
from Support.bin.snooze_helpers import parse_input
import datetime


@pytest.mark.parametrize("ds_today,x,ds_result",  [
    ("2020-06-01", "2d", "2020-06-03"),
    ("2020-06-01", "5d", "2020-06-06"),
    ("2020-06-01", "1d", "2020-06-02"),
    ("2012-12-31", "1d", "2013-01-01"),
    ("2020-02-28", "1d", "2020-02-29"),
    ("2020-02-29", "1d", "2020-03-01"),
    ("2020-06-01", "1m", "2020-07-01"),
    ("2020-06-01", "2m", "2020-08-01"),
    ("2020-06-01", "5m", "2020-11-01"),
    ("2020-06-01", "7m", "2021-01-01"),
    ("2020-06-01", "12m", "2021-06-01"),
    ("2050-11-10", "24m", "2052-11-10"),
    ("2050-11-10", "36m", "2053-11-10"),
    ("2020-01-29", "1m", "2020-02-29"),
    ("2021-01-29", "1m", "2021-03-01"),
    ("2020-12-30", "2m", "2021-03-01"),
    ("2020-12-31", "2m", "2021-03-01"),
    ("2021-07-31", "1m", "2021-08-31"),
    ("2021-07-31", "2m", "2021-10-01"),
    ("1980-01-01", "1w", "1980-01-08"),
    ("2020-11-20", "2w", "2020-12-04"),
])
def test_snooze_timespec(ds_today, x, ds_result):
    today = datetime.datetime.strptime(ds_today, "%Y-%m-%d")
    snoozedate = parse_input(x, today)
    assert snoozedate.strftime("%Y-%m-%d") == ds_result


@pytest.mark.parametrize("ds_today,x,ds_result",  [
    ("2020-12-03", "tom", "2020-12-04"),
    ("2020-12-03", "fri", "2020-12-04"),
    ("2020-12-03", "sat", "2020-12-05"),
    ("2020-12-03", "sun", "2020-12-06"),
    ("2020-12-03", "mon", "2020-12-07"),
    ("2020-12-03", "tue", "2020-12-08"),
    ("2020-12-03", "wed", "2020-12-09"),
    ("2020-12-03", "thu", "2020-12-10"),
    ("2020-12-28", "sat", "2021-01-02"),
])
def test_snooze_timespec_weekdays_tom(ds_today, x, ds_result):
    today = datetime.datetime.strptime(ds_today, "%Y-%m-%d")
    snoozedate = parse_input(x, today)
    assert snoozedate.strftime("%Y-%m-%d") == ds_result


@pytest.mark.parametrize("ds", [
    ("-1m"),
    ("xyx"),
    ("3x"),
    (""),
    ("27l"),
])
def test_specparsing_invalid(ds):
    with pytest.raises(ValueError):
        parse_input(ds)


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
    None,
])
def test_dateparsing_invalid(ds):
    with pytest.raises(ValueError):
        parse_input(ds)


def test_unspecified_snooze():
    snoozedate = parse_input("ff")

    assert snoozedate is not None
    assert snoozedate.strftime("%Y-%m-%d") == "1900-01-01"

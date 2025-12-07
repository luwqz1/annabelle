from annabelle.unit._unit import Unit, UnitType


SECONDS = Unit(
    type=UnitType.SECONDS,
    per_sec=1,
    forms=frozenset({"s", "sec", "secs", "second", "seconds"}),
)
MINUTES = Unit(
    type=UnitType.MINUTES,
    per_sec=60,
    forms=frozenset({"m", "min", "mins", "minute", "minutes"}),
)
HOURS = Unit(
    type=UnitType.HOURS,
    per_sec=3_600,
    forms=frozenset({"h", "hr", "hrs", "hour", "hours"}),
)
DAYS = Unit(
    type=UnitType.DAYS,
    per_sec=86_400,
    forms=frozenset({"d", "dy", "dys", "day", "days"}),
)
WEEKS = Unit(
    type=UnitType.WEEKS,
    per_sec=604_800,
    forms=frozenset({"w", "wk", "wks", "week", "weeks"}),
)
MONTHS = Unit(
    type=UnitType.MONTHS,
    per_sec=2_629_746,
    forms=frozenset({"mo", "mos", "month", "months"}),
)
YEARS = Unit(
    type=UnitType.YEARS,
    per_sec=31_556_926,
    forms=frozenset({"y", "yr", "yrs", "year", "years"}),
)

ALL_UNITS = (
    SECONDS,
    MINUTES,
    HOURS,
    DAYS,
    WEEKS,
    MONTHS,
    YEARS,
)
"""All units for English"""

__all__ = (
    "ALL_UNITS",
    "SECONDS",
    "MINUTES",
    "HOURS",
    "DAYS",
    "WEEKS",
    "MONTHS",
    "YEARS",
)

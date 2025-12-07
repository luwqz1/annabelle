from annabelle.unit._unit import Unit, UnitType


SECONDS = Unit(
    type=UnitType.SECONDS,
    per_sec=1,
    forms=frozenset({"с", "сек", "секунда"}),
    use_morph=True,
)
MINUTES = Unit(
    type=UnitType.MINUTES,
    per_sec=60,
    forms=frozenset({"м", "мин", "минута"}),
    use_morph=True,
)
HOURS = Unit(
    type=UnitType.HOURS,
    per_sec=3_600,
    forms=frozenset({"ч", "час"}),
    use_morph=True,
)
DAYS = Unit(
    type=UnitType.DAYS,
    per_sec=86_400,
    forms=frozenset({"д", "день"}),
    use_morph=True,
)
WEEKS = Unit(
    type=UnitType.WEEKS,
    per_sec=604_800,
    forms=frozenset({"н", "нед", "неделя"}),
    use_morph=True,
)
MONTHS = Unit(
    type=UnitType.MONTHS,
    per_sec=2_629_746,
    forms=frozenset({"мес", "месяц"}),
    use_morph=True,
)
YEARS = Unit(
    type=UnitType.YEARS,
    per_sec=31_556_926,
    forms=frozenset({"г", "год"}),
    use_morph=True,
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
"""All units for Russian"""

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

from __future__ import annotations

import dataclasses
import datetime
import re
import typing

from annabelle.unit import Unit, UnitType

if typing.TYPE_CHECKING:
    from collections.abc import Iterable


class ParsedTime(dict[UnitType, int]):
    _PER_SEC: typing.ClassVar[dict[UnitType, int]] = {
        UnitType.SECONDS: 1,
        UnitType.MINUTES: 60,
        UnitType.HOURS: 3_600,
        UnitType.DAYS: 86_400,
        UnitType.WEEKS: 604_800,
        UnitType.MONTHS: 2_629_746,
        UnitType.YEARS: 31_556_926,
    }

    @property
    def total_seconds(self) -> int:
        return sum(
            value * self._PER_SEC[unit_type]
            for unit_type, value in self.items()
        )

    def to_timedelta(self) -> datetime.timedelta:
        return datetime.timedelta(seconds=self.total_seconds)

    def to_datetime(self, base: datetime.datetime | None = None) -> datetime.datetime:
        if base is None:
            base = datetime.datetime.now(datetime.timezone.utc)
        return base + self.to_timedelta()


WORD_TO_NUM_RU: dict[str, int] = {
    "ноль": 0,
    "один": 1,
    "одна": 1,
    "одну": 1,
    "два": 2,
    "две": 2,
    "три": 3,
    "четыре": 4,
    "пять": 5,
    "шесть": 6,
    "семь": 7,
    "восемь": 8,
    "девять": 9,
    "десять": 10,
    "одиннадцать": 11,
    "двенадцать": 12,
    "тринадцать": 13,
    "четырнадцать": 14,
    "пятнадцать": 15,
    "шестнадцать": 16,
    "семнадцать": 17,
    "восемнадцать": 18,
    "девятнадцать": 19,
    "двадцать": 20,
    "тридцать": 30,
    "сорок": 40,
    "пятьдесят": 50,
    "шестьдесят": 60,
    "семьдесят": 70,
    "восемьдесят": 80,
    "девяносто": 90,
    "сто": 100,
}

WORD_TO_NUM_EN: dict[str, int] = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
}

WORD_TO_NUM = WORD_TO_NUM_RU | WORD_TO_NUM_EN
TOKEN_PATTERN = re.compile(r"\d+|[a-zA-Zа-яА-ЯёЁ]+")


@dataclasses.dataclass(slots=True)
class Parser:
    units: tuple[Unit, ...]

    def __init__(self, units: Iterable[Unit], /) -> None:
        self.units = tuple(units)

    def _parse_number(self, token: str) -> int | None:
        if token.isdigit():
            return int(token)
        lower = token.lower()
        if lower in WORD_TO_NUM:
            return WORD_TO_NUM[lower]
        return None

    def _find_unit(self, token: str) -> Unit | None:
        for unit in self.units:
            if unit.match(token):
                return unit
        return None

    def parse(self, text: str) -> ParsedTime:
        tokens = TOKEN_PATTERN.findall(text)
        parsed = ParsedTime()

        i = 0
        while i < len(tokens):
            token = tokens[i]

            num = self._parse_number(token)
            if num is not None:
                if i + 1 < len(tokens):
                    unit = self._find_unit(tokens[i + 1])
                    if unit:
                        parsed[unit.type] = parsed.get(unit.type, 0) + num
                        i += 2
                        continue
                i += 1
                continue

            unit = self._find_unit(token)
            if unit is not None:
                if i + 1 < len(tokens):
                    num = self._parse_number(tokens[i + 1])
                    if num is not None:
                        parsed[unit.type] = parsed.get(unit.type, 0) + num
                        i += 2
                        continue

                if i > 0:
                    num = self._parse_number(tokens[i - 1])
                    if num is not None and unit.type not in parsed:
                        parsed[unit.type] = num
                        i += 1
                        continue
            i += 1

        return parsed


__all__ = ("Parser", "ParsedTime")

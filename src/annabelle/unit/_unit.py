from __future__ import annotations

import dataclasses
import enum
import typing

from mawo_pymorphy3 import MAWOMorphAnalyzer

MORPH: typing.Final = MAWOMorphAnalyzer()


class UnitType(enum.StrEnum):
    SECONDS = "seconds"
    MINUTES = "minutes"
    HOURS = "hours"
    DAYS = "days"
    WEEKS = "weeks"
    MONTHS = "months"
    YEARS = "years"


@dataclasses.dataclass(frozen=True, slots=True)
class Unit:
    type: UnitType
    per_sec: int
    forms: frozenset[str]
    use_morph: bool = False

    def match(self, word: str) -> bool:
        word_lower = word.lower()

        if word_lower in self.forms:
            return True

        if self.use_morph:
            parsed = MORPH.parse(word_lower)
            if parsed:
                normal_form = parsed[0].normal_form
                if normal_form in self.forms:
                    return True

        return False


__all__ = ("UnitType", "Unit", "MORPH")

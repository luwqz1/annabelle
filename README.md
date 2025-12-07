```python
from annabelle import Parser, unit

>>> string = '/ban @username 1 h 37 min 15 sec "Violating server rules"'
>>> parser = Parser(unit.en.ALL_UNITS)
>>> res = parser.parse(string)

>>> res
{<UnitType.HOURS: 'hours'>: 1, <UnitType.MINUTES: 'minutes'>: 37, <UnitType.SECONDS: 'seconds'>: 15}

>>> res.total_seconds
5835

>>> res.to_timedelta()
datetime.timedelta(seconds=5835)

>>> res.to_datetime()  # total_seconds + now date time
datetime.datetime(2025, 12, 7, 20, 17, 31, 5502, tzinfo=datetime.timezone.utc)
```

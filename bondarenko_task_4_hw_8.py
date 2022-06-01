"""познакомиться с модулем datetime и написать программу с помощью lambda
для возвращение текущего года, месяца , дня
например результат должен быть таким
import datetime
now = datetime.datetime.now()
.....ваш код))
print(year(now))
print(month(now))
print(day(now))"""

import datetime
from typing import Any

now = datetime.datetime.now()
#2022-06-01 18:51:06.097293

year: Any = lambda i: i.year
month: Any = lambda i: i.month
day: Any = lambda i: i.day

print(year(now))
print(month(now))
print(day(now))

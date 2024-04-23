import re
from datetime import datetime

date_string = "26.03.2000"
#date_string = "07.10.2023"
date_pattern = r"(\d+)/(\d+)/(\d+)"
date_pattern2 = r"(\d+).(\d+).(\d+)"

match = re.search(date_pattern, date_string)
match2 = re.search(date_pattern2, date_string)
day, month, year = [0]*3

if match:
    day, month, year = match.groups()
    #print(f"Day: {day}, Month: {month}, Year: {year}")
elif match2:
    day, month, year = match2.groups()
    #print(f"Day: {day}, Month: {month}, Year: {year}")
else:
    print("Invalid date format")
    exit(0)

current_date = datetime.now()
year, month, day = int(year), int(month), int(day)
target_date = datetime(year, month, day)

delta = current_date - target_date

years_passed = delta.days // 365
days_passed = delta.days % 36

a = str(years_passed) + "г. " if years_passed != 0 else ""
b = str(days_passed) + "д. "
c = f" ({delta.days+1}д.)"
print(a+b+c)
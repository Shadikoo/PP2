#1 Python program to subtract five days from current date.
from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)

print("Current date:", current_date.strftime("%Y-%m-%d"))
print("Five days ago:", five_days_ago.strftime("%Y-%m-%d"))

#2 Python program to print yesterday, today, tomorrow.
from datetime import datetime, timedelta

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:    ", today)
print("Tomorrow: ", tomorrow)

#3 Python program to drop microseconds from datetime.
from datetime import datetime

now = datetime.now()
without_microseconds = now.replace(microsecond=0)

print("With microseconds:   ", now)
print("Without microseconds:", without_microseconds)

#4  Python program to calculate two date difference in seconds.
from datetime import datetime

date1 = datetime(2025, 2, 1, 12, 0, 0)
date2 = datetime(2025, 2, 26, 15, 30, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print(f"Difference between {date2} and {date1}:")
print(f"{seconds} seconds")
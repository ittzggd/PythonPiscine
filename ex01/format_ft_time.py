from time import time
from datetime import date

current_time = time()

today = date.today()
#returns a string representing date and time using date, time or datetime object.
today_frmt = today.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {current_time:,.4f}  or {current_time:.2e} in scientific notation")
print(today_frmt)

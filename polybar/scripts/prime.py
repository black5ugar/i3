"""
is today a prime?
"""

from time import strftime, time, localtime

# print(strftime("%Y%m%d", gmtime()))
# get the date

date = strftime("%Y.%m.%d", localtime(time()))
today = int(strftime("%Y%m%d", localtime(time())))

for i in range(2, today):
    if (today % i) == 0:
        print(f"Today: {date} is not a prime")
        break
else:
    print(f"Today: {date} is a prime")

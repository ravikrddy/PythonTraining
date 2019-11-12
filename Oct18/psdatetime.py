import datetime

rdate = '25/06/2013  6:10:50 PM'

print(datetime.datetime.strptime(rdate, '%d/%m/%Y %I:%M:%S %p'))
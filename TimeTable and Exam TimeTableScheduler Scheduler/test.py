# Python program to find yesterday,
# today and tomorrow
  
  
# Import datetime and timedelta
# class from datetime module
from datetime import datetime, timedelta
  
  
# Get today's date
presentday = datetime.now() # or presentday = datetime.today()

Today = presentday.strftime('%Y%m%d')
Year = Today[0:4]
Month = Today[4:6]
Day = Today[6:8]
  
  
# strftime() is to format date according to
# the need by converting them to string
print("Today", Today, '\n',"Year ",Year,'\n', 'Month ',Month,'\n', 'Day',Day)
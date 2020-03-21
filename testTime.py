from datetime import date
from dateutil.relativedelta import relativedelta


since_date = str(date.today() - relativedelta(months=+1))

print(since_date)
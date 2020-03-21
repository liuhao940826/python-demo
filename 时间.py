from datetime import date

from dateutil.relativedelta import relativedelta

time= str(date.today() - relativedelta(months=+3))
print(time)
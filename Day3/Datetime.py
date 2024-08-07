#DateTime

from datetime import datetime, timedelta
def generate_dates(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date.strftime("%Y-%m-%d")
        current_date += timedelta(days=1)
start_date = datetime(2024, 5, 1)
end_date = datetime(2024, 6, 30)

for date in generate_dates(start_date, end_date):
    print(date)

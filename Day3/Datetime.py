#DateTime

from datetime import datetime, timedelta
def generate_dates(start_date, end_date):
    curr_date = start_date
    while curr_date <= end_date:
        yield curr_date.strftime("%Y-%m-%d")
        curr_date += timedelta(days=1)
start_date = datetime(2024, 5, 1)
end_date = datetime(2024, 6, 30)

for date in generate_dates(start_date, end_date):
    print(date)

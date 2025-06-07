from datetime import datetime,timedelta
def display_current_datetime():
    current_date = datetime.today()
    current_date=current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)
display_current_datetime()

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    days_diff=timedelta(days=days)
    future_date=current_date+days_diff
    future_date=future_date.strftime("%Y-%m-%d")
    print(future_date)
calculate_future_date()    
# made using chatGPT

from datetime import datetime, timedelta

# Function to check if a date is a holiday or weekend
def is_school_day(date, holidays, exclude_saturdays, exclude_sundays):
    if date in holidays:
        return False
    if exclude_saturdays and date.weekday() == 5:  # Saturday
        if (date.day - 1) // 7 == 1:  # Second Saturday
            return False
    if exclude_sundays and date.weekday() == 6:  # Sunday
        return False
    return True

# Given data
start_date = datetime(2024, 6, 21)
end_date = datetime(2024, 10, 1)
holidays = {datetime(2024, 7, 17), datetime(2024, 8, 15), datetime(2024, 8, 26),
            datetime(2024, 9, 9), datetime(2024, 9, 10), datetime(2024, 9, 11), datetime(2024, 9, 12),
            datetime(2024, 9, 16)}

# List of school attendance days provided by the user
attendance_dates = [
    datetime(2024, 6, 24), datetime(2024, 6, 25), datetime(2024, 6, 27),
    datetime(2024, 7, 1), datetime(2024, 7, 4), datetime(2024, 7, 6), datetime(2024, 7, 8), datetime(2024, 7, 9),
    datetime(2024, 7, 12), datetime(2024, 7, 18), datetime(2024, 7, 20), datetime(2024, 7, 22), datetime(2024, 7, 29),
    datetime(2024, 7, 31), datetime(2024, 8, 2), datetime(2024, 8, 5), datetime(2024, 8, 6), datetime(2024, 8, 8),
    datetime(2024, 8, 12), datetime(2024, 8, 13), datetime(2024, 8, 14), datetime(2024, 8, 20), datetime(2024, 8, 21),
    datetime(2024, 8, 23), datetime(2024, 8, 27), datetime(2024, 8, 28), datetime(2024, 8, 30), datetime(2024, 8, 31),
    datetime(2024, 9, 2), datetime(2024, 9, 3), datetime(2024, 9, 6), datetime(2024, 9, 7), datetime(2024, 9, 21),
    datetime(2024, 9, 23), datetime(2024, 9, 24), datetime(2024, 9, 25), datetime(2024, 9, 26), datetime(2024, 9, 28),
    datetime(2024, 10, 3)
]

# Check for total school days and actual attendance days
total_school_days = 0
attended_days = 0
date = start_date

# Count the total school days and attendance days
while date <= end_date:
    if is_school_day(date, holidays, exclude_saturdays=True, exclude_sundays=True):
        total_school_days += 1
        if date in attendance_dates:
            attended_days += 1
    date += timedelta(days=1)

print(total_school_days, attended_days)

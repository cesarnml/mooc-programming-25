# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date


def list_years(dates: list[date]):
    return sorted([x.year for x in dates])

from datetime import date, time, datetime
#calling the roday
#function of the date class
today=date.today()
now=datetime.now()
print("today's date is ",today)
print("\nCurrent Date and Time is ",now)

#printing date's components
print("\nDate components",today.year,today.month,today.day)
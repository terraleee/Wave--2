month = input("Enter the name of the month: ")
days = 31

if month == "April" or month == "June" or month == "September" or month == "November" :
    days = 30
elif month == "February" :
    days = "28 or 29"

print("The month of", month, "has", days, "days in it.") 
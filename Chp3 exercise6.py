month = int(input("Enter a month (in numeric): "))
day = int(input("Enter a day (in numeric): "))
year = int(input("Enter a 2-digit year: "))
if month * day == year:
    print("The date is magic")
else:
    print("The date is not magic")

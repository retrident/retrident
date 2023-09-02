def main():

   principal = float(input("Enter the amount of principal amount to be deposited: "))

   rate = float(input("Enter annual interest rate paid by the account: "))

   num = int(input("Enter the number of times per year that the interest is compunded: "))

   years = float(input("Enter the number of years the account will be left to earn interest: "))

   amount = principal*(1+(rate*.01)/num)**(num*years)  

   print("The amount of money will be in the account after ", years, "years:", round(amount,2))

main()

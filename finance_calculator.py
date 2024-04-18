""" finance_calculators.py pseudo code

import math
display the two options and ask user to pick which part of the program they would like to use
 use or operator to give options
use else if user doesn't enter appropriate option and end program

if investment, ask:
 amount they're depositing # store as inv_amount
 the interest rate # store as inv_int_rate
 number of years for investment # store as inv_time

 ask user to choose between simple or compound interest
  use or operator to give options
 input numbers into appropriate formulas which I store as a certain value
print message displaying the value the user will be expectant to get

if bond, ask:
 value of house # store as val_house
 the interest rate # store as bond_interest
 number of months to repay # store as bond_time
print message displaying the amount the user must repay
"""

import math

print("\nPlease read the options below and type what financial calculator you'd like to use:")
print("\nInvestment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan") # providing context for what the user will be using
option = input("\nWhich option do you choose?\n")


if option == "investment" or option == "Investment" or option == "INVESTMENT": # Using the "or" operator to give options
 print("\n" + "-" * 30) # I will use these to create space and segment the output
 inv_amount = int(input("\nEnter your initial investment amount: "))
 inv_int_rate = float(input("Enter your interest rate (the % is not needed): ")) / 100 # divided by 100 to create the percentage
 inv_time = int(input("Enter how many years are you planning on investing for: "))
 print("\n" + "-" * 30)               

 print("\nWhat type of interest are you using? A reminder:")
 print("Simple interest is continually calculated on the initial amount invested and is only calculated once per year. This interest amount is then added to the amount that you initially invested")
 print("Compound interest is different, in that the interest is calculated on the current total known as the accumulated amount.")
 interest_type = input() # Putting this input on another line to aid with spacing

 if interest_type == "simple" or interest_type == "Simple" or interest_type == "SIMPLE": # creating the options for the response
  # making the formula for simple interest
  simple_amount = (inv_amount * (1 + (inv_int_rate * inv_time))) 
  simple_amount_rounded = round(simple_amount, 2) # Using the round to provide the pennies if the calculation provides a number with multiple decimal places
  print("\n" + "-" * 30)
  print(f"\nIn over a period of {inv_time} years, your investment of £{inv_amount} will return £{simple_amount_rounded}.")
  print("\n" + "-" * 30)
  
 elif interest_type == "compound" or interest_type == "COMPOUND" or interest_type == "Compound":
  # making the formula for compound interest
  comp_amount = round(inv_amount * math.pow((1 + inv_int_rate), inv_time), 2) # attempted a different way to round the numbers to 2 decimal places
  print("\n" + "-" * 30)
  print(f"\nOver a period of {inv_time} years, your investment of £{inv_amount} will return £{comp_amount}.")
  print("\n" + "-" * 30)

elif option == "Bond" or option == "bond" or option == "BOND": # Coding alternative option for bond calculator
 print("\n" + "-" * 30)
 house_value = float(input("Enter the value of the home: "))
 bond_int_rate = ((float(input("Enter the annual interest rate: "))) / 12) / 100 # Divided by 12 to get the monthly interest and divided by 100 to get the percent
 monthly_time = float(input("Enter the number of months over which the bond will be repaid: "))
 """ (I found that the formula using these numbers didn't work when I cast them as integers. Floats for some reason worked. Welcome feedback on this) """
 print("\n" + "-" * 30)

 repayment = (bond_int_rate * house_value) / (1 - (1 + bond_int_rate) ** -monthly_time) # # making the formula for bond calculators
 print("\n" + "-" * 30)
 print(f"\nIn order to pay back your loan of £{house_value} over a period of {monthly_time} months, you must pay an average of £{repayment:.2f} per month.")
 print("\n" + "-" * 30)
 
 



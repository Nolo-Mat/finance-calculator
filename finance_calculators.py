import math 

# Displaying information necessary for the user to make their first decision.
print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
print("investment  -  to calculate the amount of interest you'll earn on your investment.")
print("bond        -  to calculate the amount you'll have to pay on a home loan.")
calculation_type =  str(input("Enter: "))

choice = calculation_type.lower()  # Changing the users input to lowercase 

# Conditionals ment to prompt the user for the input necessary for investment calculations
if choice == "investment":
    deposit = float(input("\nEnter the amount you want to deposit: R"))
    interest_rate = float(input("\nEnter your interest rate percentege: "))
    num_of_years = int(input("\nEnter the number of years that you plan on investing for: "))
    interest_type = str(input("\nWould you like 'compound' or 'simple' interest: "))
    
    int_type = interest_type.lower()  # Changing the users input to lowercase
    
    # Multiplying by 0.01 and Dividing by 100 have the same result.  
    int_rate = interest_rate * 0.01  # Convering the interest rate to a decimal.
    
    # Calculating and displaying the final amount for simple interest
    if int_type == "simple":
        final_amount = deposit * (1 + int_rate * num_of_years)
        print(f"Your final amount is:\n R{round(final_amount, 2)}")
        
    # Calculating and displaying the final amount for compound interest
    elif int_type == "compound":
        final_amount = deposit * math.pow((1 + int_rate), num_of_years)
        print(f"Your final amount is:\n R{round(final_amount, 2)}")

    else:
        print("\nInvalid Entry. Please enter a valid option.")


# Conditionals ment to prompt the user for the input necessary for bond calculations
elif choice == "bond":
    house_value = int(input("\nEnter the present value of your house: R"))
    interest_rate = float(input("\nEnter your interest rate percentege: "))
    repay_months = int(input("\nEnter the number of months you plan to take to repay the bond: "))
    
    monthly_int_rate = (interest_rate * 0.01) / 12  # Converting the annual interest to monthly interest.
    
    # Calculating and displaying the monthly repayment rate. 
    repayment = (monthly_int_rate * house_value) / (1 - (1 + monthly_int_rate)**(-repay_months))
    
    # Rounding of and displaying the final monthly repayment.
    print(f"\nYour monthly bond repayment is: R{round(repayment, 2)}")  
else:
    print("\nInvalid Entry. Please enter a valid option.")    
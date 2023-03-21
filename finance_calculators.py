import math

print("""investment - to calculate the amount of interest you'll earn on your investment 
bond - to calculate the amount you'll have to pay on a home loan""")

# Taking user choice for investment or bond
selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Using "lower" to ensure input can be used regardless of capitalisation
user_selection = selection.lower()


# First, screen for incorrect input
if user_selection != 'investment' and user_selection != 'bond':
    print("Your choice was not recognised. Please select a valid option from the menu above.")

# If user chooses to calculate investment:
elif user_selection == 'investment':

    # Specifying float/int will cause error if % or £ included, for example, as well as allow to calculate with inputs
    starting_money = float(input("Please enter the amount you are investing: "))
    interest_rate = float(input("Please enter the interest rate: "))
    years = int(input("Please enter the number of years you wish to invest for: "))
    interest = input("Please specify if you wish this to be simple or compound interest: ")
    interest_type = interest.lower()

    if interest_type == 'simple':
        # Formula to calculate simple interest, rounded for presentability
        total_simple = starting_money*(1 + (interest_rate/100)*years)
        total_simple = round(total_simple, 2)
        print(f"If you invest £{starting_money} for {years} years at a rate of {interest_rate}%, you will have £{total_simple}.")

    elif interest_type == 'compound':
        # Formula to calculate compound interest, rounded for presentability
        total_compound = starting_money * math.pow((1 + (interest_rate/100)), years)
        total_compound = round(total_compound, 2)
        print(f"If you invest £{starting_money} for {years} years at a rate of {interest_rate}%, you will have £{total_compound}.")

    else:
        print("You did not specify a valid type of interest.")


# If user chooses to calculate bond:
elif user_selection == 'bond':

    house_value = float(input("Please enter the current value of the house: "))
    interest_rate = float(input("Please enter your interest rate: "))
    months = int(input("Please enter the number of months for repayment: "))

    # Formula for bond repayments, rounded for presentability
    repayment = ((interest_rate/100) * house_value) / (1 - (1 + (interest_rate/100))**(months*-1))
    repayment = round(repayment, 2)
    print(f"If you wish to repay your house valued at £{house_value} at a rate of {interest_rate}% over {months} months, your monthly repayment will be £{repayment}.")

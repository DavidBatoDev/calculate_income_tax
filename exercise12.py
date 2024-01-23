# Function to calculate income tax based on income
def calculate_income_tax(income):
    # Initialize tax payable to 0
    tax_payable = 0
    # Check if income is less than or equal to 10000
    # If yes, no tax payable, return 0
    if income <= 10000:
        return tax_payable
    # Check if income is less than or equal to 20000
    # Calculate tax payable for the portion between 10001 and 20000 at 10%
    elif income <= 20000:
        tax_payable = (income - 10000) * 10 / 100
    # If income is greater than 20000
    # Calculate tax payable for the second 10000 at 10%
    # Calculate tax payable for the portion above 20000 at 20%
    else:
        tax_payable = 10000 * 10 / 100
        tax_payable += (income-20000) * 20 / 100
    # Return the total tax payable
    return tax_payable

print(calculate_income_tax(45000)) # 6000.0


    

    


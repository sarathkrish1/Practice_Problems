#car loan payment
def calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    number_of_payments = loan_term_years * 12
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
    return monthly_payment

# Get user input
loan_amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
loan_term_years = int(input("Enter the loan term (in years): "))

# Calculate monthly payment
monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years)
# Display the result
print(f"The monthly payment for the car loan is: ${monthly_payment:.2f}")       
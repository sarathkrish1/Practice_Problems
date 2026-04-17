#emi calculation using genai copilot
#logical block 1: function to calculate interest for a given principal, rate and time with validation
def calculate_interest(principal, rate, time):
    if principal <= 0 or rate <= 0 or time <= 0:
        raise ValueError("Principal, rate, and time must be positive numbers.")
    
    interest = (principal * rate * time) / 100
    return round(interest, 2)
#logical block 2: function to calculate total amount after adding interest to principal
def calculate_total_amount(principal, interest):
    total_amount = principal + interest
    return round(total_amount, 2)
#logical block 3: function to calculate EMI based on total amount, rate and time
def calculate_emi(total_amount, rate, time):
    monthly_rate = rate / 1200
    months = time * 12
    
    emi = (total_amount * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    return round(emi, 2)
#logical block 4: main function to get user input, validate and call the above functions
def main():
    principal_entered = input("Enter the principal amount: ")
    roi_entered = input("Enter the rate of interest (annual %): ")
    years_entered = input("Enter the time period in years: ")

    # ----- VALIDATION + CONVERSION -----
    principal = int(principal_entered) if principal_entered.isdigit() else None
    roi = int(roi_entered) if roi_entered.isdigit() else None
    years = int(years_entered) if years_entered.isdigit() else None

    if principal is not None and roi is not None and years is not None:
        interest = calculate_interest(principal, roi, years)
        total_amount = calculate_total_amount(principal, interest)
        emi = calculate_emi(total_amount, roi, years)

        print(f"\nCalculated Interest: {interest}")
        print(f"Total Amount to be Paid: {total_amount}")
        print(f"Monthly EMI: {emi}")
    else:
        print("\n❌ Invalid input! Please enter positive numeric values only.")
if __name__ == "__main__":
    main()  

                    
    
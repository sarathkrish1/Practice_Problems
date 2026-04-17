# -------------------------------
# EMI CALCULATOR (CLEAN VERSION)
# -------------------------------

# ----- INPUT -----
principal_entered = input("Enter the Principal (₹): ")
roi_entered = input("Enter the Rate of Interest (% per year): ")
years_entered = input("Enter the Time (in years): ")


# ----- VALIDATION + CONVERSION -----
principal = int(principal_entered) if principal_entered.isdigit() else None
roi = int(roi_entered) if roi_entered.isdigit() else None
years = int(years_entered) if years_entered.isdigit() else None


# ----- MAIN LOGIC -----
if (principal is not None and roi is not None and years is not None
        and principal > 0 and roi > 0 and years > 0):

    # Monthly interest rate
    monthly_rate = roi / (12 * 100)

    # Total months
    months = years * 12

    # EMI Formula
    emi = round(
        principal * monthly_rate * (1 + monthly_rate) ** months /
        ((1 + monthly_rate) ** months - 1), 2)

    # Initial balance
    balance = principal

    # ----- TABLE HEADER -----
    print("\n" + "-" * 65)  
    print(f"| {'Month':^5} | {'EMI':^10} | {'Interest':^10} | {'Principal':^12} | {'Balance':^12} |")
    print("-" * 65)

    # Totals
    total_emi = total_interest = total_principal = 0

    # ----- EMI SCHEDULE -----
    for month in range(1, months + 1):

        interest = round(balance * monthly_rate, 2)
        principal_paid = round(emi - interest, 2)

        # Fix rounding issue in last month
        if month == months:
            principal_paid = balance
            emi_last = round(principal_paid + interest, 2)
            balance = 0
            current_emi = emi_last
        else:
            balance = round(balance - principal_paid, 2)
            current_emi = emi

        # Accumulate totals
        total_emi += current_emi
        total_interest += interest
        total_principal += principal_paid

        # Print row
        print(f"| {month:^5} | {current_emi:^10.2f} | {interest:^10.2f} | {principal_paid:^12.2f} | {balance:^12.2f} |")

    # ----- TOTALS -----
    print("-" * 65)
    print(f"| {'Total':^5} | {total_emi:^10.2f} | {total_interest:^10.2f} | {total_principal:^12.2f} | {'-':^12} |")
    print("-" * 65)

else:
    print("\n❌ Invalid input! Please enter positive numeric values only.")
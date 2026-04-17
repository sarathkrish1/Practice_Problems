import json
#monthly rate function
def calculate_monthly_rate(roi):
    return roi/1200

#emi function
def calculate_emi(principle,roi,time):
    months=time*12
    rate=calculate_monthly_rate(roi)
    emi = (
        principle * rate * (1 + rate) ** months
        / ((1 + rate) ** months - 1)
    )

    return round(emi, 2)

#emi details function
def compute_emi_details(principle,roi,time):
    emi_details=[]
    months=time*12
    rate=calculate_monthly_rate(roi)
    emi=calculate_emi(principle,roi,time)
    balance=principle

    for month in range(1,months+1):
        emi_dict={}

        interest=round((balance*rate),2)
        principle_paid=round(emi-interest,2)

        if month == months:
            principle_paid = balance
            emi_last = principle_paid + interest
            balance = 0
            current_emi = round(emi_last, 2)
        else:
            balance = round(balance - principle_paid, 2)
            current_emi = emi

        # Store data
        emi_dict["Month"] = month
        emi_dict["EMI"] = current_emi
        emi_dict["Interest"] = interest
        emi_dict["Principal"] = principle_paid
        emi_dict["Balance"] = balance

        emi_details.append(emi_dict)

    return emi_details
#TEST
emi_details = compute_emi_details(10000, 10, 1)

print("EMI Details:\n")
for row in emi_details:
    print(row)

print("\nJSON Format:")
print(json.dumps(emi_details, indent=2))
def calculate_monthly_rate(roi):
    return roi/1200
def calculate_emi(principle,roi,time):
    months=time*12
    interest_per_month=calculate_monthly_rate(roi)
    emi=(
        principle * interest_per_month * (1 + interest_per_month) ** months
        / ((1 + interest_per_month) ** months - 1)
    )
    return round(emi, 2)

# Test
print(f"EMI for Principal: 1000, ROI: 10, Years: 1 is {calculate_emi(1000, 10, 1)}")
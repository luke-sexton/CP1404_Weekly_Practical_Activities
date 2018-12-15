title_message = "Electricity bill estimator"
print(title_message)

cents_per_kWh = int(input("Enter cents per kWh: "))
daily_use_in_kWh = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

# convert cents_per_kWh input to cents integer
cents_input_conversion = cents_per_kWh / 100

daily_use_calculation = cents_input_conversion * daily_use_in_kWh
estimated_bill_calculation = daily_use_calculation * billing_days

print("Estimated bill: ${}".format(estimated_bill_calculation))
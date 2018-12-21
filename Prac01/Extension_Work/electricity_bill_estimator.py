TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")

# cents_per_kWh = int(input("Enter cents per kWh: ")) [Original Code]
valid_tariff_input = False
tariff_input = int(input("Which tariff? 11 or 31: "))

while not valid_tariff_input:
    if tariff_input == 11:
        chosen_tariff = TARIFF_11
        valid_tariff_input = True
    elif tariff_input == 31:
        chosen_tariff = TARIFF_31
        valid_tariff_input = True
    else:
        print("Invalid input")
        tariff_input = int(input("Which tariff? 11 or 31: "))

daily_use_in_kWh = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))


# convert cents_per_kWh input to cents integer [Original Code]
# cents_input_conversion = cents_per_kWh / 100 [Original Code]

# daily_use_calculation = cents_input_conversion * daily_use_in_kWh [Original Code]
daily_use_calculation = chosen_tariff * daily_use_in_kWh
estimated_bill_calculation = daily_use_calculation * billing_days

print("Estimated bill: ${:.2f}".format(estimated_bill_calculation))

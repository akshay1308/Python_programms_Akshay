electricity_unit = float(input("Enter Electricity Units:"))
if electricity_unit <= 50:
    electricity_unit_charges = electricity_unit * 0.50
    print("Your Electricity Bill is Rs:", electricity_unit_charges)
elif electricity_unit <= 100:
    electricity_unit_charges = electricity_unit * 0.75
    print("Your Electricity Bill is Rs:", electricity_unit_charges)
elif electricity_unit <=250:
    electricity_unit_charges = electricity_unit * 1.25
    print("Your Electricity Bill is Rs:", electricity_unit_charges)
else:
    electricity_unit_charges = electricity_unit * 1.5
    additional_surcharge = (0.17 * electricity_unit_charges)
    electricity_unit_with_sutcharge = electricity_unit_charges + additional_surcharge
    print("Your Electricity Bill is Rs:", electricity_unit_with_sutcharge)








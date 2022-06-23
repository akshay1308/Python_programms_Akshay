electricity_unit = float(input("Enter Electricity Units: "))
def calculate_bill(n: float) -> float:
    if n <= 50:
        return n * 0.50
    elif n <= 100:
        return n * 0.75
    elif n <= 250:
        return n * 1.25
    else:
        return n * 0.5 + (0.17 * n)
print("Your Electricity Bill is Rs:", calculate_bill(electricity_unit))

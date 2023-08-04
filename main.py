def years_to_months(age_in_years: int) -> int:
    return age_in_years * 12


def starts_with_capital_case(name: str) -> bool:
    return name.capitalize() == name


age = int(input("How old are you? (in years)"))
print(f"You are {years_to_months(age)} months old")

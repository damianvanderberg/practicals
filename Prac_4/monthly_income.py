"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of monthly_."""
    incomes = []
    monthly_ = int(input("How many monthly_? "))

    for monthly_ in range(1, monthly_ + 1):
        income = float(input("Enter income for monthly_ {} :".format(monthly_)))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for mon in range(1, monthly_ + 1):
        income = incomes[monthly_ - 1]#why -1
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(monthly_, income, total))


main()
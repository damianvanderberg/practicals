"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of how_many_months."""
    incomes = []
    how_many_months = int(input("How many months? "))

    for month in range(1, how_many_months + 1):
        income = float(input("Enter income for month {} :".format(month)))
        incomes.append(income)

    income_report(incomes)


def income_report(incomes):
    """"report indicating incomes and running total after each month"""

    print("\nIncome Report\n-------------")
    total = 0  # running total of income after inputs
    for month, income in enumerate(incomes): #enumerate adds a counter for each iterate in the brackets (income)
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month+1, income, total))


main()

def budget_paycheck(paycheck):
    housing_transportation = 0.45 * paycheck
    food = 0.15 * paycheck
    savings = 0.15 * paycheck
    taxes = 0.25 * paycheck
    return (housing_transportation, food, savings, taxes)

def main():
    paycheck = float(input("Please enter your paycheck: "))
    ht, fd, sv, tx = budget_paycheck(paycheck)
    print("\n\nBudget\n{}\n{}\n{}\n{}\n{}".format(
          "="*20,
          "Housing/transportation: $" + str(round(ht)),
          "Food: $" + str(round(fd)),
          "Savings: $" + str(round(sv)),
          "Taxes: $" + str(round(tx))))
         

main()

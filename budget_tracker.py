import locale as lc     #import locale library
lc.setlocale(lc.LC_ALL,"en_US") #set locale to US locale

def monthly_income():       #function to obtain monthly income
    while True:             #loops until a valid amount is input; loop ends with returning the income
        try:
            income = float(input("Input monthly income: $"))
            if income < 0:
                raise ValueError("Income cannot be negative")   #Custom error raised if income is below 0
            else:
                return income
        except Exception as e:      #Error is raised if the input value can't be converted to a float
            print(f"Invalid input: {e}; Please enter a valid income")


def user_expenses():        #function to obtain the user's expenses 
    total_expenses = []
    while (expense := input("Enter expense amount or 0 to finish: $")) != '0':      #input repeats until the user enters 0
        try:
            expense = float(expense)
            if expense < 0:
                raise ValueError("Expense cannot be negative")      #Custom error raised if income is below 0
            else:
                total_expenses.append(expense)
        except Exception as e:      #Error is raised if the input value can't be converted to a float
            print(f"Invalid input: {e}; Please enter a valid expense")
    return total_expenses


def main():     #create main function
    print("Welcome to the Budget Tracker" +     #declare purpose of prgm
          '\n' + "-"*35)
    income = monthly_income()   #obtain income with function
    expenses = user_expenses()  #obtain expenses with function
    remaining_budget = income - sum(expenses)   #caluclate the remaining budget from the income and sum of the expenses
    print("\nBudget Results:" +     #output the income, sum of expenses, and remaining budget formatted with f-string formats
          "\n" + "-"*35 +
          f"\nTotal Income: ${income:,.2f}"+
          f"\nExpenses: ${sum(expenses):,.2f}" +
          f"\nRemaining Budget: ${remaining_budget:,.2f}")
    
    print("\nComplete Expense List:\n" + "-"*35)
    for index, expense in enumerate(expenses):      #loop to output all of the expenses in order of input
        print(f"{index+1}. {lc.currency(expense, grouping=True)}")  #output the expenses formatted using the locale library, according to the US locale


if __name__=="__main__":
    main()
    print("\nCompleted by, Jeremiah Vela")

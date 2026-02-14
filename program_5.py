# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

# Pseudocode – Program #5: Bank Balance
# Ask user for monthly budget
# Input budget
# totalExpenses = 0
# WHILE user has more expenses
#     Ask user to enter an expense
#     Add expense to totalExpenses
# END WHILE
# IF totalExpenses > budget
#     Display "You are over budget by $" (totalExpenses - budget)
# ELSE
#     Display "You are under budget by $" (budget - totalExpenses)
# END IF
def main():

    budget = 0.0
    difference = 0.0
    spent = 1.0         # initialize for while loop
    total = 0.0

    budget = float(input("Enter your monthly budget: "))

    while spent != 0:
        spent = float(input("Enter an expense (0 to finish): "))
        total += spent

    difference = budget - total

    if difference > 0:
        print("You are under budget by $" + str(difference))
    elif difference < 0:
        print("You are over budget by $" + str(abs(difference)))
    else:
        print("You spent exactly your budget.")

if __name__ == '__main__':
    main()
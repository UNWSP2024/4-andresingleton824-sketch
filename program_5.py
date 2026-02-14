# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    budget = float(input("Enter your monthly budget: "))

    while spent != 0:
        spent = float(input("Enter an expense (0 to finish): "))
        total += spent

    difference = budget - total

    if difference > 0:
        print("You are under budget by $", difference)
    elif difference < 0:
        print("You are over budget by $", abs(difference))
    else:
        print("You spent exactly your budget.")


if __name__ == '__main__':
    main()
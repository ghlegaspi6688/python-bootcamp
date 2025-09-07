def spend(expenses):
    """TODO: Add a new cost in expenses"""
    expense = int(input("Enter Spending: "))
    expenses.append(expense)

def refund(expenses):
    """TODO: Remove the last cost added (if any)"""
    #lv1 = len
    expenses.pop(-1)
def show(expenses):
    """TODO: Print the current list of expenses and total"""
    #print(sum(expenses))
    print(expenses)
def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ")
        if command == "spend":
            spend(current_expenses)
        elif command == "refund":
            refund(current_expenses)
        elif command == "show":
            show(current_expenses)
        elif command == "end":
            running = False
main()

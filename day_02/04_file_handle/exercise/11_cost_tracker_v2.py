# def spend(expenses):
#     """TODO: Add a new cost in expenses"""
#
#
# def refund(expenses):
#     """TODO: Remove the last cost added (if any)"""
#
#
# def show(expenses):
#     """TODO: Print the current list of expenses and total"""
#
#
# def save(expenses):
#     """TODO: Save the current list of expenses to a new file"""
#
#
# def main():
#     running = True
#     current_expenses = []
#
#     while running:
#         command = input("Command: ")
#         if command == "spend":
#             spend(current_expenses)
#
#
# main()


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
def save(expenses):
    with open("expenses.txt", "w") as file:
        for exp in expenses:
            exp = str(exp)
            file.write(exp + "\n")
def load():
    with open("expenses.txt", "r") as file:
        file_contents = file.readlines()
        expenses = []
        for exp in file_contents:
            exp = exp.replace("\n", "")
            exp = int(exp)
            expenses.append(exp)
    return expenses
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
        elif command == "save":
            save(current_expenses)
        elif command == "load":
            current_expenses = load()
main()
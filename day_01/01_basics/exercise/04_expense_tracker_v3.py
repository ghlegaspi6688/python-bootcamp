# TODO: Ask the user for three values
expense_1 = int(input("num 1: "))  # Let the user enter a number
expense_2 = int(input("num 2: "))  # Let the user enter a number
expense_3 = int(input("num 3: "))  # Let the user enter a number

# TODO: Then, print each information one line at a time
print(expense_1)
print(expense_2)
print(expense_3)

total = expense_1 + expense_2 + expense_3
print(total)

# TODO: Format this part using f-strings
print(expense_1, "+", expense_2, "+", expense_3, "=", total)

# TODO: Ask the user for three values
expense_1 = input("Enter Input 1:")  # Let the user enter a number
expense_2 = input("Enter Input 2:")  # Let the user enter a number
expense_3 = input("Enter Input 3:")  # Let the user enter a number

# TODO: Then, print each information one line at a time
print(expense_1)
print(expense_2)
print(expense_3)

exp1 = int(expense_1)
exp2 = int(expense_2)
exp3 = int(expense_3)
tot = exp1 + exp2 + exp3

print(f"{expense_1} + {expense_2} + {expense_3} = {tot}")

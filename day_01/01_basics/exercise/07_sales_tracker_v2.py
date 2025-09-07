# TODO: Ask the user how many items will be calculated
#input_count = None
#total = 0

# TODO: Use a for loop to ask for more than one cost and count
#item_cost = None  # Let the user enter a number
#item_count = None  # Let the user enter a number
#item_total = item_cost + item_count

#print(total)

item_cost1 = int(input("Enter cost of item 1: ")) # Let the user enter a number
item_count1 = int(input("Enter population of item 1: "))  # Let the user enter a number
item_cost2 = int(input("Enter cost of item 2: "))  # Let the user enter a number
item_count2 = int(input("Enter population of item 2: "))  # Let the user enter a number
item_cost3 = int(input("Enter cost of item 3: "))  # Let the user enter a number
item_count3 = int(input("Enter population of item 3: "))  # Let the user enter a number

total = (item_cost1 * item_count1) + (item_cost2 * item_count2) + (item_cost3 * item_count3)
print(total)


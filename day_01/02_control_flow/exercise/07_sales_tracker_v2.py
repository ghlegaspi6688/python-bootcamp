# TODO: Ask the user how many items will be calculated
#input_count = None
input_count = int(input("Enter No of Input: "))
#count = 0
total = 0

# TODO: Use a for loop to ask for more than one cost and count
for _ in range(input_count):
    #count++
    item_cost = float(input("Enter Item Cost: "))
    item_count = int(input("Enter No of Item/s: "))
    item_total = item_cost * item_count
    print(item_total)
    total = total + item_total
#item_cost = None  # Let the user enter a number
#item_count = None  # Let the user enter a number
#item_total = item_cost + item_count

print(total)



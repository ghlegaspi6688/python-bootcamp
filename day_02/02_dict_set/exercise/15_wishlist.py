# TODO: Fill in the details of the item you plan to buy
order = {
    "Name": "Epyon",
    "Info": "Red close range HG",
    "Cost": 3000
    # "Name": "Deathscythe",
    # "Info": "Black close range HG",
    # "Cost": 3500
    # "Name": "Leo",
    # "Info": "Green Mass Production Gen Purpose",
    # "Cost": 1500
}

# TODO: Print the item details in the following format:
"""
Order:
	Name: item name
	Info: item info
	...
"""
for subject, description in order.items():
    print(subject + ":", description)

# TODO: Fill in the details of the items you plan to buy
order = [
    {
        "Name": "Epyon",
        "Info": "Red close range HG",
        "Cost": 3000,
    },
    {
        "Name": "Deathscythe",
        "Info": "Black close range HG",
        "Cost": 3500,
    },
    {
        "Name": "Leo",
        "Info": "Green Mass Production Gen Purpose",
        "Cost": 1500,
    }
]


# TODO: Print the item details in the following format (for each order):
"""
Order:
	Name: item name
	Info: item info
	...
"""
for item in order:
    #print(item)
    print("\t Name:", item['Name'])
    print("\t Info:", item['Info'])
    print("\t Cost:", item['Cost'])

for ord in order:
    for nam1, nam2 in ord.items():
        print(nam1, nam2)
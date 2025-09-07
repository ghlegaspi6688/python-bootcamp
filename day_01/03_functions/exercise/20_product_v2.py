
def product(v1, v2, v3 = 1):
    """ TODO: Takes three inputs (or two) and print the product"""
    tot = v1 * v2 * v3
    return tot

# TODO: product(1, 1, 1)	# 1
# TODO: product(1, 2, 3)	# 6
# TODO: product(2, 5, 10)	# 100
# TODO: product(3, 3)	    # 9
# TODO: product(2, 5)	    # 12

v1 = int(input("Enter first number: "))
v2 = int(input("Enter second number: "))
v3 = int(input("Enter third number: "))

print(product(v1,v2, v3))
# Create the binary for letter 'h' as a list of 1’s and 0’s
binary_h = list(bin(ord('h')))
binary_h = binary_h[2:]

# Create the binary for letter 'a' as a list of 1’s and 0’s
binary_a = list(bin(ord('a')))
binary_a = binary_a[2:]

# TODO: Create the binary for 'hahaha'
#binary = []
#print(binary)

#for binary_h, binary_a in zip(binary_h, binary_a):
#    print(f"{binary_h}{binary_a}")

#print(binary_h)
#print(binary_a)

binary_ha = binary_h + binary_a
print(binary_ha * 3)
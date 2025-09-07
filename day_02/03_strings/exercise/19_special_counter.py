string = input('Enter string: ')
special_count = 0
special_char = '!@#$%^&*()'

# TODO: Add one to special_count for each special char in string
#special_count += 1
#print(special_count)
for str in string:
     if str in special_char:
         special_count = special_count + 1
     else:
         pass
    #print(str)

print(special_count)
    # ask = input("Enter word: ")
    # if ask in banned_words:
    #     print("Banned")
    # else:
    #     pass
    # print("Banned")
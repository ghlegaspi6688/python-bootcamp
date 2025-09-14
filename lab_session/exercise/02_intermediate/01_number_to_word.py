from num2words import num2words

#def number_to_words(n: int) -> str:
"""
    Converts an integer into its English word representation.
    Example: 42 → "forty-two"

    Note: Only handle from 0 to 999,999
    """

    # if n > 0 and n < 999999:
    #     #get length
    #     pop1 = len(str(n))
    #     pop2 = str(n)
    #     popr = pop2[-3:-1]
    #     popl = pop2[-6:-4]
    #     #thousands =
    #     #slice, right three first
    #     if pop1 <= 3:
    #         if n == 10:
    #             return "ten"
    #         elif n == 11:
    #             return "eleven"
    #         elif n == 12:
    #             return "twelve"
    #         else:
    #             print(popr[-1])
    #             print(popr[1])
    #             print(popr[2])
    #
    #         #processed1 = threenum(n)
    #         #print(pop1)
    #         #print(pop2)
    #         #print(popr)
    #     #sliced, left three
    #     else:
    #     #return "number within range"
    #         #pass
    #         return popl
    # else:
    #     return "Input Invalid"

#def threenum(m: int)



ones = {
    "9": "nine",
    "8": "eight",
    "7": "seven",
    "6": "six",
    "5": "five",
    "4": "four",
    "3": "three",
    "2": "two",
    "1": "one",
}
tens = {
    "9": "ninety",
    "8": "eighty",
    "7": "seventy",
    "6": "sixty",
    "5": "five",
    "4": "four",
    "3": "three",
    "2": "two",
    "1": "one",
}

num = int(input("Enter Number: "))
print(num2words(num))
#print(number_to_words(num))
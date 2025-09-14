def count_vowels(string: str) -> int:
    """Return the number of vowels in the given string"""
    pass
count = 0;
vowel = ['a', 'e', 'i', 'o', 'u']
user_input = input("Enter word: ")
user_input = user_input.lower()
for user_inputs in user_input:
    #print(user_inputs)
    for vowels in vowel:
        if user_inputs == vowels:
            count += 1
        else:
            pass
print(f"Total Number of vowels: {count}")
banned_words = ("moist", "break", "raise")

# TODO: Ask the user for a word
# TODO: If the word is in banned_words, say "Banned"

ask = input("Enter word: ")
if ask in banned_words:
    print("Banned")
else:
    pass
#print("Banned")

import random

#first, just open the file and output the words to a list. we'll separate into difficulty later.
with open("words.txt") as file:
    string = file.read()
    full_word_list = string.split()
    
#then given the full word list, choose a random word and assign it to the mystery word variable

mystery_word = random.choice(full_word_list)
print(mystery_word)

print(len(mystery_word))
print("_" * len(mystery_word))

#then write a function that counts the number of characters in the mystery word string, and prints to screen a number of underscores equal to the length of that string.

#then capture user input for the guessed letter. need a loop where if the guessed character is in the word, it will print the location of the guessed letter to screen, replacing the underscore. if not, it will increment the wrong guess count up one. then return to the beginning of the loop UNLESS the guess count has been reached. if it has, then break and print the "you lost" message.
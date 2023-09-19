#######################paired programmming###############################
# Juan Garcia and Mia Juarez
# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.
magic = 'abracadabra'
print(magic[5])
print(magic[-1])
print(magic.find("c"))

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet.find("hij"))
print(alphabet[7:10])
alphabet2 = "abcdefghijklm"
print(alphabet2[0::2])
print(alphabet[::-1])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy "
print(quote[-16:-1])

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
quoteTwo = "Python is fun. Fun is good. Good is subjective."
print(quoteTwo[-11:-1])
words = quoteTwo.split()
third_word = words[2::3]
print(third_word)
reversedWords = ''.join(words[::-1])
print(reversedWords)

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
low = "MAY THE FORCE BE WITH YOU."
print(low.lower())
print(low.upper())

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
motto = ["Make", "haste", "slowly."]
finalstring = ''.join(motto)
print(finalstring)
print(finalstring.split('a'))

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
life = "Life is what happens when you are busy making other plans."
print(life.replace("busy", "distracted"))
print(life.replace("plans", "mistakes"))

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
repitition = "Iteration " * 5
print(repitition)


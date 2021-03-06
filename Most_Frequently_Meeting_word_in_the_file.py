# File: Most_Frequently_Meeting_word_in_the_file.py
# Description: Most Frequently Meeting word in the file
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Most Frequently Meeting word in the file // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Most_Frequently_Meeting_word_in_the_file (date of access: XX.XX.XXXX)


# Implementing the task - find the most frequently meeting word from the file
# Reading the lines from the file and putting them to the string in one line
string = ''
with open('dataset_3363_3.txt') as inf:
    for line in inf:
        string += line.strip()
        string += ' '

# Putting all in lowecase letters
# It is important to use split() in order to write the words in the set but not the letters
string = string.lower().split()
print(string)  # Checking if the string was created properly

# Creating a set and writing in it the string
# The repeated elements will not be written
s = set(string)  # Creating the set with elements from the string but it will not add repeated elements
# print(s)  # Checking if the set was created properly
frequent = string[0]
f = 1
# Going through the elements of the set
for x in s:
    if string.count(x) > f:
        f = string.count(x)
        frequent = x
    if string.count(x) == f and x < frequent:
        frequent = x

print()
print(frequent, f)


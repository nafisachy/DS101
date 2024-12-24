import re

text = "This is a good day"

# search and find a word
if re.search("good", text):
    print("wonderful!")
else:
    print("alas! :(")

# take out a word
text = "Amy works diligently. Amy gets good grades. Our student Amy is successful."
print(re.split("Amy", text))

# How many times does the word appear
print(re.findall("Amy", text))

# caret match and confirm the word appears in the beginning of every line
print(re.search("^Amy", text))


grades = "ACAAAABCBCBAADABAAABD"
print(re.findall("B", grades))

# set specifies how many times one or more text appear
print(re.findall("[AB]", grades))

# how many times the first text followed by a text in the range of characters in the next set
print(re.findall("[A][B-D]", grades))

# number of times either pattern of text appear
print(re.findall("AB|AC", grades))

# caret inside the set negates the previous rule and parse out only text that did not include the character
print(re.findall("[^B]", grades))

# caret inside and outside the set refers to parsing text that did not start with A
print(re.findall("^[^A]", grades))

# how many times did it appear back to back- 2x to 10x
print(re.findall("A{2,10}", grades)) # DO NOT put space with curly brackets


# The following are just different ways of getting the same results
# 2 A's followed immediately by 2 more A's
print(re.findall("A{1,1}A{1,1}", grades))

# Shorter way of doing
print(re.findall("A{2,2}", grades))

# Simple
print(re.findall("AA", grades))

print(re.findall("A{2}", grades))

# decreasing trend
print(re.findall("A{1,10}B{1,10}C{1,10}", grades))

data= "abc"
print(re.findall)
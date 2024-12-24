import re

with open("ferpa", "r") as file:
    wiki=file.read()

# get a list all of the headers
# characters between a-z or A-Z
# 1-100 of those characters
# followed by [edit]
print(re.findall("[a-zA-Z]{1,100}\[edit\]", wiki))

# \w- metacharacter- includes any letter and digits and numbers
print(re.findall("[\w]{1,100}\[edit\]", wiki))

# * - any number of times
print(re.findall("[\w]*\[edit\]", wiki))

# add spaces
print(re.findall("[\w ]*\[edit\]", wiki))

for title in re.findall("[\w ]*\[edit\]", wiki):
    # split [] out fo the title and get the first value
    print(re.split("[\[]", title)[0])



# redoing by grouping ()
print(re.findall("([\w ]*)(\[edit\])", wiki))

# returns a tuple
for item in re.finditer("([\w ]*)(\[edit\])", wiki):
    print(item.groups())

# return group of one
for item in re.finditer("([\w ]*)(\[edit\])", wiki):
    print(item.group(1))




for item in re.finditer("(?P<title>[\w ]*)(?P<edit_link>\[edit\])", wiki):
    # by dictionary
    print(item.groupdict()['title'])
    print(item.groupdict())

# + is whitespace
# match but don't capture (use ?= look ahead)
for item in re.finditer("(?P<title>[\w ]+)(?=\[edit\])", wiki):
    print(item)




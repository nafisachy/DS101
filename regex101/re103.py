import re
import chardet

with open("buddhist", "r", encoding="utf-8") as file:
    wiki = file.read()


# the university title with any character .*
# location indicator
# city of university with word character \w*
# separator
# state
pattern = """
(?P<title>.*)        #the university title
(–\ located\ in\ )   #an indicator of the location
(?P<city>\w*)        #city the university is in
(,\ )                #separator for the state
(?P<state>\w*)       #the state the city is located in"""

# multi-lined pattern
for item in re.finditer(pattern,wiki,re.VERBOSE):
    print(item.groupdict())
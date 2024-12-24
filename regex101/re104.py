import re

with open("nytimeshealth", "r", encoding="utf-8") as file:
    health=file.read()

# hash, word characters, digits, asteriks and any number of those, look ahead (followed by but not match) any white space
pattern = '#[\w\d]*(?=\s)'

print(re.findall(pattern, health))
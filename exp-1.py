import re

text = "My phone number is 9876543210"

# Search for a 10-digit number
result = re.search(r'\d{10}', text)

if result:
    print("Number found:", result.group())
else:
    print("Number not found")

# Match a word at the beginning
result = re.match(r'My', text)

if result:
    print("Pattern matched:", result.group())
else:
    print("Pattern not matched")

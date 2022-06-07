import re

test = 'Rijksweg 44 6533XT Amsterdam'
match = re.search(r"\b\d{4}[A-Z]{2}\b", test, re.IGNORECASE)
if match:
    print(match.group())
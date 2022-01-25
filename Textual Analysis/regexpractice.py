import re

text = 'Here is an example sentence. This sentence is an example!'
test = re.search('sentence', text)
print(test)
print(test.start())
print(test.end())
print(test.group())

test = re.split('sentence', text)
print(test)

test = re.findall('sentence', text)
count = len(test)
print(test, count)

test = re.sub('sentence', 'phrase', text)
print(test)

# special patterns
text = "You miss 100% of the shots you do1n't take - Wayne Gretzky - Michael Scott"
test = re.findall(r'\w+', text)
print(test)

test = re.findall(r'[A-Z][a-z]+', text)
print(test)

test = re.findall(r'\b[a-z][a-z][a-z][a-z]\b', text)
print(test)

test = re.findall(r'\b[a-z]{4}\b', text)
print(test)

test = re.sub(r'\b[a-z]{4}\b', 'XXXX', text)
print(test)

test = re.findall(r'\d+', text) #include +: search for all digits until it sees a boundary like a space
print(test)

test = re.findall(r'[0-9]', text)
print(test)

test = re.findall(r'shots .* take', text) #give anything in between shots & take (inclusive)
print(test)

text = """Scott, Michael - Regional Manager
Schrute, Dwight - Salesperson
Halpert, Jim - Salesperson
Beesly, Pam - Receptionist
Howard, Ryan - Temp
Bernard, Andy - Salesperson
Hudson, Stanley - Salesperson
Malone, Kevin - Accountant
Palmer, Meredith - Supplier Relations
Martin, Angela - Accountant
Martinez, Oscar - Accountant
Lapin, Phyllis - Salesperson
Kapoor, Kelly - Customer Service
Flenderson, Toby - Human Resources Representative
Bratton, Creed - Quality Control
Philbin, Darryl - Foreman
"""
print(text)

names = re.findall(r'[A-Z][a-z]+,\s[A-Z][a-z]+', text)
print(names)

# add parantheses for first&last names
names = re.findall(r'([A-Z][a-z]+),\s([A-Z][a-z]+)', text)
print(names)

# convert to FirstName LastName - Job Position  // \1 refers to first captured group (last name), and \2 refers to first name
names = re.sub(r'([A-Z][a-z]+),\s([A-Z][a-z]+)', r'\2 \1', text) # substituted into a format that we intended!
print(names)


## Exercise
text = 'The student was taking ENG 101, ACC 200, FIN 101, and MTH 114.'
words = re.findall(r'\w+', text)
print(words)

new_text = re.sub(r'\d+', 'NUMBER', text)
print(new_text)

courses = re.findall(r'[A-Z][A-Z][A-Z]\s[0-9][0-9][0-9]', text)
print(courses)

courses = re.findall(r'[A-Z]{3}\s\d{3}', text)
print(courses)

l = re.findall(r'student .* 200', text)
print(l)

# regex group exercises
text = """801-123-4567
706-124-8765
714-321-9876"""

names = re.findall(r'(\d{3})-(\d{3})-(\d{4})', text)
print(names)

format = re.sub(r'(\d{3})-(\d{3})-(\d{4})',r'(\1)\2-\3', text)
print(format)
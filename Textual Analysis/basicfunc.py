text = "Hello World!! "
replaced_text = text.replace('Hello', 'Hi')
print(replaced_text)
stripped_text1 = text.strip()
print(stripped_text1)
stripped_text2 = stripped_text1.strip("!")
print(stripped_text2)
words = text.split(' ')
print(words)
text_upper = text.upper()
print(text_upper)
text_lower = text.lower()
print(text_lower)

# count occurrences
text = "Hello World Hello!"
count_hello = text.count("Hello")
print(count_hello)
words = ['Hello', 'World', '!']
joined_text = '~'.join(words)
print(joined_text)

# search strings
text = 'Here is a string. This string is an example string.'
loc_string = text.find('string')
print(loc_string)

text = 'hello world'
print('The text is all lower case     : '+str(text.islower()))
print('The text is all upper case     : '+str(text.isupper()))
print('The text is all numeric        : '+str(text.isnumeric()))
print('The text is all alphabetic     : '+str(text.isalpha()))
print('The text is all alpha-numeric  : '+str(text.isalnum()))
print('The text starts with "Hello"   : '+str(text.startswith('Hello')))
print('The text ends with "!"         : '+str(text.endswith("!")))


# Exercise
text = 'Hello Accounting Coding Camp students. I hope you are enjoying Python! Python is #1!'
string_list = ['Hello','Python','Coder']

# list of all words in text string
words = text.split()
print(words)

text = text.replace("#1", "number one")
print(text)

text = text.lower()
print(text.islower())

p_count = text.count('p')
print(p_count)

hope_loc = text.find('hope')
print(hope_loc)

print(text.endswith("."))

joined_test = " ".join(string_list)
print(joined_test)
import requests
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from MyFunctions import html_to_text

headers = {'User-Agent': 'ORGANIZATION jisangyu@uchicago.edu'}
html = requests.get('https://www.sec.gov/Archives/edgar/data/320193/000119312511282113/d220209d10k.htm',headers=headers).text
text = html_to_text(html)
print(text)

words = word_tokenize(text)
words = [w for w in words if w.isalpha()]
num_words = len(words)
print(num_words)
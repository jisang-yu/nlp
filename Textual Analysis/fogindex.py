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

sents = sent_tokenize(text)
sent_list = [s for s in sents if len(s.split(" "))>3]
num_sents = len(sent_list)
print(num_sents)

import nltk
nltk.download('cmudict')

from nltk.corpus import cmudict
cmu = cmudict.dict()
# print(cmu)

word = 'disclosure'
print(cmu[word.lower()])

word_pronunciation = ''.join(cmu[word.lower()][0])
print(word_pronunciation)

num_syl = len(re.findall(r'\d', word_pronunciation))

def num_syllables(word):
    try:
        word_pronunciation = ''.join(cmu[word.lower()][0])
        num_syl = len(re.findall(r'\d', word_pronunciation))
    except Exception:
        if len(word) >= 10:
            num_syl = 3
        else:
            num_syl = 1

    return num_syl

print(num_syllables('disclosure'))
print(num_syllables('strategically'))
print(num_syllables('interestingly'))

complex_words = [w for w in words if num_syllables(w) >= 3]
num_complex_words = len(complex_words)
print(num_complex_words)
# Calculate words per sentence
words_per_sentence = num_words/num_sents

# Calculate the percentage of complex words
percent_complex_words = (num_complex_words/num_words) * 100

# Calculate Fog
fog = 0.4 * (words_per_sentence + percent_complex_words)

print(fog)
print("---------------")


### Exercise
def fog_calculator(url):
    url = url
    headers = {'User-Agent': 'ORGANIZATION jisangyu@uchicago.edu'}
    html = requests.get(url, headers=headers).text

    text = html_to_text(html)
    text = html_to_text(html)
    words = word_tokenize(text.lower())
    words = [t for t in words if t.isalpha()]
    num_words = len(words)

    sents = sent_tokenize(text)
    sent_list = [s for s in sents if len(s.split(" ")) > 3]
    num_sents = len(sent_list)

    complex_words = [w for w in words if num_syllables(w) >= 3]
    num_compwords = len(complex_words)

    words_per_sent = num_words / num_sents
    percent_complex = (num_compwords / num_words) * 100

    fog = 0.4 * (words_per_sent + percent_complex)

    return fog

print(fog_calculator("https://www.sec.gov/Archives/edgar/data/27419/000002741920000008/tgt-20200201.htm"))
print(fog_calculator("https://www.sec.gov/Archives/edgar/data/104169/000010416920000011/wmtform10-kx1312020.htm"))
import re

import pandas as pd
import requests
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import regexp_tokenize
from collections import Counter
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# text = "I was lucky — I found what I loved to do early in life. Woz and I started Apple in my parents' garage when I was 20. We worked hard, and in 10 years Apple had grown from just the two of us in a garage into a $2 billion company with over 4,000 employees. We had just released our finest creation — the Macintosh — a year earlier, and I had just turned 30. And then I got fired. How can you get fired from a company you started? Well, as Apple grew we hired someone who I thought was very talented to run the company with me, and for the first year or so things went well. But then our visions of the future began to diverge and eventually we had a falling out. When we did, our Board of Directors sided with him. So at 30 I was out. And very publicly out. What had been the focus of my entire adult life was gone, and it was devastating. I really didn't know what to do for a few months. I felt that I had let the previous generation of entrepreneurs down — that I had dropped the baton as it was being passed to me. I met with David Packard and Bob Noyce and tried to apologize for screwing up so badly. I was a very public failure, and I even thought about running away from the valley. But something slowly began to dawn on me — I still loved what I did. The turn of events at Apple had not changed that one bit. I had been rejected, but I was still in love. And so I decided to start over. I didn't see it then, but it turned out that getting fired from Apple was the best thing that could have ever happened to me. The heaviness of being successful was replaced by the lightness of being a beginner again, less sure about everything. It freed me to enter one of the most creative periods of my life. During the next five years, I started a company named NeXT, another company named Pixar, and fell in love with an amazing woman who would become my wife. Pixar went on to create the world's first computer animated feature film, Toy Story, and is now the most successful animation studio in the world. In a remarkable turn of events, Apple bought NeXT, I returned to Apple, and the technology we developed at NeXT is at the heart of Apple's current renaissance. And Laurene and I have a wonderful family together. I'm pretty sure none of this would have happened if I hadn't been fired from Apple. It was awful tasting medicine, but I guess the patient needed it. Sometimes life hits you in the head with a brick. Don't lose faith. I'm convinced that the only thing that kept me going was that I loved what I did. You've got to find what you love. And that is as true for your work as it is for your lovers. Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle. As with all matters of the heart, you'll know when you find it. And, like any great relationship, it just gets better and better as the years roll on. So keep looking until you find it. Don't settle."
# nltk.download('punkt')
#
# words = word_tokenize(text)
# print(words)
#
# sentences = sent_tokenize(text)
# print(sentences)
#
# cap_words = regexp_tokenize(text, r'[A-Z][a-zA-Z]+') #similar to re.findall('[A-Z][a-zA-Z]+', text)
# print(cap_words)
#
# tokens = word_tokenize(text)
# counts = Counter(tokens)
# print(counts)
# print(counts.most_common())
#
# # Text Preprocessing
# stopwords_list = stopwords.words('english')
# print(stopwords_list)
#

# porter = PorterStemmer()
# words = ['caring', 'helpful', 'kindness', 'jumps']
# stemmed_list = []
# for word in words:
#     stemmed_list.append(porter.stem(word))
# print(stemmed_list)
#
# # apply to our text
# tokens = word_tokenize(text)
# tokens = [t.lower() for t in tokens]
#
# tokens = [t for t in tokens if t.isalpha()]
#
# tokens = [t for t in tokens if t not in stopwords.words('english')]
#
# tokens = [porter.stem(t) for t in tokens]
# print(tokens)
# print(Counter(tokens))
# print(Counter(tokens).most_common(5))
#
# df = pd.DataFrame.from_dict(Counter(tokens), orient='index').reset_index()
# df.rename(columns={'index':'tokens', 0:'count'}, inplace=True)
# df.sort_values(by=['count'] ,ascending=False, inplace=True)
# print(df)

## Exercise
headers = {'User-Agent': 'ORGANIZATION jisangyu@uchicago.edu'}
url = 'https://www.sec.gov/Archives/edgar/data/320193/000032019320000050/a8-kexhibit991q2202032.htm'
data = requests.get(url, headers=headers).text
print(data[0:1000])

from MyFunctions import html_to_text
text = html_to_text(data)

tokens = word_tokenize(text)
tokens = [t.lower() for t in tokens]
tokens = [t for t in tokens if t not in stopwords.words('english')]
tokens = [t for t in tokens if t.isalpha()]
porter = PorterStemmer()
tokens = [porter.stem(t) for t in tokens]
applecount = Counter(tokens)

apple_token = pd.DataFrame.from_dict(applecount, orient='index').reset_index()
apple_token.rename(columns={'index':'token', 0:'count'}, inplace=True)
apple_token.sort_values(by=['count'], ascending=False, inplace=True)
print(apple_token) #compani is the most frequent

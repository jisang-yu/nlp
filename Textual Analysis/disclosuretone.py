import pandas as pd
import re
import requests
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
from MyFunctions import html_to_text

neg_words = pd.read_excel('LoughranMcDonald_SentimentWordLists_2018.xlsx', sheet_name='Negative', header=None)
neg_words.rename(columns={0:'token'}, inplace=True)
neg_words['token']= neg_words['token'].str.lower()
print(neg_words)

pos_words = pd.read_excel('LoughranMcDonald_SentimentWordLists_2018.xlsx', sheet_name='Positive', header=None)
pos_words.rename(columns={0:'token'}, inplace=True)
pos_words['token'] = pos_words['token'].str.lower()
print(pos_words)

# Apple 2020 8-K
headers = {'User-Agent': 'ORGANIZATION jisangyu@uchicago.edu'}
url = 'https://www.sec.gov/Archives/edgar/data/320193/000032019320000050/a8-kexhibit991q2202032.htm'
apple = requests.get(url, headers=headers).text
text = html_to_text(apple)
print(text)

def get_counts(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t.isalpha()]
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    counts = Counter(tokens)
    df = pd.DataFrame.from_dict(counts, orient='index').reset_index()
    df.rename(columns={'index':'token', 0:'count'}, inplace=True)
    df.sort_values(by=['count'], ascending=False, inplace=True)

    return df

df = get_counts(text)
print(df)

#merge with negative words list
data = pd.merge(df, neg_words, on='token', how='left', indicator=True)
print(data['_merge'].value_counts())
print(data[data._merge == 'both'])

data['neg'] = 0
data.loc[data._merge=='both','neg'] = 1
data.drop(columns=['_merge'], axis=1,inplace=True)
print(data)

#merge with positive words list
data = pd.merge(data, pos_words, on='token', how='left', indicator=True)
data['pos'] = 0
data.loc[data._merge=='both', 'pos'] = 1
data.drop(columns=['_merge'], inplace=True)
print(data[data.pos == 1])

#negative, positive word count
num_neg = (data[data['neg'] == 1])['count'].sum() # data[data.neg == 1][count].sum()
num_pos = data[data.pos == 1]['count'].sum()
total_wc = data['count'].sum()

net_tone = (num_pos - num_neg)/(num_pos + num_neg)
pos_tone = num_pos / total_wc
neg_tone = num_neg / total_wc

print('Net tone is equal to {0:.3f}, and postive tone is equal to {1:.3f}'.format(net_tone, pos_tone))
print('Negative tone is equal to {:.3f}'.format(neg_tone))

# Exercises
headers = {'User-Agent': 'ORGANIZATION jisangyu@uchicago.edu'}
url1 = 'https://www.sec.gov/Archives/edgar/data/6201/000000620110000035/ar07218k.htm'
amr = requests.get(url1, headers=headers).text
text = html_to_text(amr)

# def tone_calculate(text):
dfamr = get_counts(text)
print(dfamr)

def merge_df(tone, df, word_df):
    new = pd.merge(df, word_df, on='token', how='left', indicator=True)
    new[tone] = 0
    new.loc[new._merge=='both', tone] = 1
    new.drop(columns=['_merge'], inplace=True)
    return new

neg_merged = merge_df('neg', dfamr, neg_words)
all_merged = merge_df('pos', neg_merged, pos_words)
print(all_merged)

num_neg = all_merged[all_merged.neg==1]['count'].sum()
num_pos = all_merged[all_merged.pos==1]['count'].sum()
total_wc = all_merged['count'].sum()
print(num_neg, num_pos, total_wc)

net_tone = (num_pos - num_neg)/(num_pos + num_neg)
pos_tone = num_pos / total_wc
neg_tone = num_neg / total_wc
print('Net tone is equal to {:.3f}'.format(net_tone))
print('Postive tone is equal to {:.3f}'.format(pos_tone))
print('Negative tone is equal to {:.3f}'.format(neg_tone))
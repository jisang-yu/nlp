"""
Project Explanation:
I will calculate disclosure tone for firms' earnings announcement 8-Ks in 2019 Q1
I will then calculate cumulative abnormal returns for the [0,+1] window surrounding the earnings announcement date,
and test the relation between earnings announcement tone and cumulative abnormal returns.
"""

import numpy as np
import requests
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import statsmodels.api as sm
from MyFunctions import html_to_text
import os
from tqdm import tqdm

neg_words = pd.read_excel('LoughranMcDonald_SentimentWordLists_2018.xlsx', sheet_name = "Negative", header=None)
pos_words = pd.read_excel('LoughranMcDonald_SentimentWordLists_2018.xlsx', sheet_name = "Positive", header=None)
for df in [neg_words, pos_words]:
    df.rename(columns={0:'token'}, inplace=True)
    df = df['token'].str.lower()

def get_counts(text):
    # Create tokens
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t.isalpha()]
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    counts = Counter(tokens)

    # Create DataFrame of our token counts
    df = pd.DataFrame.from_dict(counts, orient='index').reset_index()
    df.rename(columns={'index':'token', 0:'count'}, inplace=True)
    df.sort_values(by=['count'], ascending=False, inplace=True)

    return df

def get_tone(url):
    headers = {'User-Agent': 'ORGANIZATION jisangyu@uchicago.edu'}
    disclosure = requests.get(url, headers=headers).text
    text = html_to_text(disclosure)

    # Get Token Count dataframe
    df = get_counts(text)

    # Merge with positive dictionary
    data = pd.merge(df, pos_words, on='token', how='left', indicator=True)
    data['pos'] = 0
    data.loc[data._merge=='both', 'pos'] = 1
    data.drop(columns=['_merge'], inplace=True)

    # Merge with negative dictionary
    data = pd.merge(data, neg_words, on='token', how='left', indicator=True)
    data['neg'] = 0
    data.loc[data._merge == 'both', 'neg'] = 1
    data.drop(columns=['_merge'], inplace=True)

    # Calculate the number of positive and negative tokens, and total number of tokens
    num_neg = data[data['neg']==1]['count'].sum()
    num_pos = data[data['pos']==1]['count'].sum()

    # Calculate tone
    net_tone = (num_pos - num_neg) / (num_pos + num_neg)

    return net_tone

# Import Earnings Announcement 8-K URLs
urls = pd.read_csv("8-K URLs.txt", sep='|')

# Compute Tone
urls['net_tone'] = np.nan
print(urls.info())

file1 = open('tone.txt', 'w')
file1.write('cik|ticker|date_filed|url|net_tone\n')
file1.close()

dones1 = open('tone.txt').readlines()
dones = {}
for done in dones1:
    try:
        cik = done.split('|')[0]
        date_filed = done.split('|')[2]
        dones[cik+'|'+date_filed] = 1
    except Exception:
        pass



for index, row in tqdm(urls.iterrows()):
    cik = str(row['cik'])
    ticker = row['ticker']
    date_filed = row['date_filed']
    url = row['URL']
    try:
        done = dones[cik+'|'+date_filed]
    except Exception:
        done = 0

    if done == 0:
        try:
            net_tone = get_tone(url)
            file1 = open('tone.txt','a')
            file1.write(cik+'|'+ticker+'|'+date_filed+'|'+url+'|'+str(net_tone)+'\n')
            file1.close()
        except Exception:
            print(cik)

data = pd.read_csv('tone.txt', sep='|', parse_dates=['date_filed'])

### Now we test whether net_tone effects CAR (Cumulative Abnormal Returns)

ret = pd.read_csv('ret.csv', parse_dates=['Date'])
ret['abnret'] = ret['ret'] - ret['ewret']
ret.sort_values(by=['ticker', 'Date'], ascending=[True, False], inplace=True)

ret['abnret_lead1'] = ret.groupby('ticker')['abnret'].shift(1)

ret['car01'] = ((ret['abnret']+1) * (ret['abnret_lead1']+1)) - 1


### merge two dataframes, data and ret
data = pd.merge(data, ret, left_on=['ticker', 'date_filed'], right_on = ['ticker', 'Date'], how='inner')
data.dropna(inplace=True)

### Finally, we run Basic OLS regression of CAR on net_tone
print(data[['net_tone', 'car01']].describe())
X = data["net_tone"]
y = data["car01"]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())
# CAR = 0.0205*NetTone + 0.0064, both coeeficient and constant statisticall significant
# As a result, there is a positive and statistically significant relation between net_tone and car01.
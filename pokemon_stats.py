import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = 'https://play.limitlesstcg.com/decks'
res = requests.get(url)

# print(res.text)
print(res.status_code)

soup = BeautifulSoup(res.content, 'html.parser')
table = soup.find('table', class_='meta')

df = pd.read_html(url, attrs = {'class': 'meta'}, flavor='bs4', thousands='.')[0]
df['Wins'] = df.Score.apply(lambda x: int(x.split(' - ')[0]))
df['Losses'] = df.Score.apply(lambda x: int(x.split(' - ')[1]))
df['Ties'] = df.Score.apply(lambda x: int(x.split(' - ')[2]))
df['Total Games'] = df['Wins'] + df['Losses'] + df['Ties']
df['Loss %'] = df['Losses'] / df['Total Games']
df['Tie %'] = df['Ties'] / df['Total Games']
df['Win % \excluding ties'] = df['Wins'] / (df['Wins'] + df['Losses'])
df['Loss % \excluding ties'] = df['Losses'] / (df['Wins'] + df['Losses'])
df = df.sort_values(by=['Win % \excluding ties'], ascending=False)

print(df.head(10))
# for row in table.tbody.find_all('tr'):
#     columns = row.find_all('td')

        

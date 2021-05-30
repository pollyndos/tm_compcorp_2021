import pandas as pd

df = pd.read_csv(r"\desktop\wiki_prep2.csv")
corpus = df[['en', 'ru']]

stop_en = ['also', 'century', 'year', 'new', 'one', 'first', 'two']
stop_ru = 'первый два один век'.split()
data_en = [[x for x in str(s).split() if len(x) > 2 and x not in stop_en] for s in corpus.en]
data_ru = [[x for x in str(s).split() if len(x) > 2 and x not in stop_ru] for s in corpus.ru]

result = ''
for i in range(len(data_ru)):
    result += f'\n{i}' + ' ' + 'RU' +'\t' + ' '.join(data_ru[i])

with open('ru_all.txt', 'w', encoding='utf8') as f:
    f.write(result)
    
    
result = ''
for i in range(len(data_en)):
    result += f'\n{i}' + ' ' + 'EN' +'\t' + ' '.join(data_en[i])

with open('en_all.txt', 'w', encoding='utf8') as f:
    f.write(result)
    
import csv

with open("job_skills.csv",encoding="utf-8") as file:
    datas=list(csv.DictReader(file))

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
pattern = re.compile(r'\s|,|\.|!|\?|:|;|\\|‘|’|\/')

words=[]
words_each=[]
lemmatizer = WordNetLemmatizer()
for d in datas:
    t=[lemmatizer.lemmatize(x.lower()) for x in re.sub(pattern,' ', d["Minimum Qualifications"]).split()]
    words_each.append(t)
    words+=t

 
sr = stopwords.words('english')
freq = nltk.FreqDist(words)
freq_sorted=[w for w in sorted(freq.items(),reverse=True,key=lambda x:x[1]) if w[0] not in sr and len(w[0])>1]

results=[]
for k,v in freq_sorted[:30]:
    c=0
    for ws in words_each:
        if k in ws:
            c+=1
    results.append({'n':k,'tc':v,'jc':c})

#绘图
from pyecharts import WordCloud

n=[res['n'] for res in results]
v=[res['tc'] for res in results]
wordcloud = WordCloud(width=1200, height=600)
wordcloud.add("最低条件", n, v, word_size_range=[40, 200])
wordcloud.render("最低条件词云.html")

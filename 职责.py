import csv

with open("job_skills.csv",encoding="utf-8") as file:
    datas=list(csv.DictReader(file))

#职责
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
pattern = re.compile(r'\s|,|\.|!|\?|:|;|\\|‘|’')

words=[]
words_each=[]
lemmatizer = WordNetLemmatizer()#提取词汇
for d in datas:
    t=[lemmatizer.lemmatize(x.lower()) for x in re.sub(pattern,' ', d["Responsibilities"]).split()]
    words_each.append(t)
    words+=t

 
sr = stopwords.words('english')
freq = nltk.FreqDist(words)
freq_sorted=[w for w in sorted(freq.items(),reverse=True,key=lambda x:x[1]) if w[0] not in sr]

#取前30个
#for key,val in freq_sorted[:30]: 
#    print (str(key) + ':' + str(val))
results=[]
for k,v in freq_sorted[:30]:
    c=0
    for ws in words_each:
        if k in ws:
            c+=1
    results.append({'n':k,'tc':v,'jc':c})

#绘图
from pyecharts import Scatter
def custom_formatter(params):
    return params.value[2]

v1=[i['tc'] for i in results]
v2=[i['jc'] for i in results]
n=[i['n'] for i in results]
scatter = Scatter("职责")
scatter.add("",v1,v2,
            is_visualmap=True,visual_type="size",
            visual_range_size=[5, 20],
            visual_dimension=0,extra_name=n,
            visual_orient="horizontal",tooltip_formatter=custom_formatter,
            visual_range=[0,1000]
            )
scatter.render("职责.html")

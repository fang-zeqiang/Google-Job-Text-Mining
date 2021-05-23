import csv
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
from collections import Counter

#对职责中的高频词汇，取有效值进行人工分类，各取五个
rt={'管理决策':['manage','strategy','solution','management','lead'],
    '技术':['develop','technical','cloud','client','build'],
    '市场营销':['product','business','customer','sale','marketing']
    }


with open("data/job_skills.csv",encoding="utf-8") as file:
    datas=list(csv.DictReader(file))

def getCounts(s:str,c:dict):
    return c.get(s,0)

sr = stopwords.words('english')
pattern = re.compile(r'\s|,|\.|!|\?|:|;|\\|‘|’')
lemmatizer = WordNetLemmatizer()

scores=[]

for d in datas:
    category=d['Category'].strip()
    t=[lemmatizer.lemmatize(x.lower()) for x in re.sub(pattern,' ', d["Responsibilities"]).split()]
    #跳过无相关内容项
    if len(t)==0:
        continue
    freq = nltk.FreqDist(t)
    tmp={}
    for i in rt.keys():
        tmp[i]=sum(map(lambda s:getCounts(s,freq),rt[i]))/len(t)
    tmp['n']=category
    scores.append(tmp)

catagorys=set([d['Category'].strip() for d in datas])
cs=dict(zip(catagorys,[[0,0,0,0]]*len(catagorys)))#counts,管理决策,技术,市场营销
for k in cs:
    cs[k]=cs[k][:]#深拷贝
for i in scores:
    cs[i['n']][0]+=1
    cs[i['n']][1]+=i['管理决策']
    cs[i['n']][2]+=i['技术']
    cs[i['n']][3]+=i['市场营销']

#聚类
from sklearn.cluster import KMeans

datasets=[]
name=[]
for k,v in cs.items():
    name.append(k)
    datasets.append(list(map(lambda x:x/v[0]*100,v[1:])))

kmeans=KMeans(n_clusters=3, random_state=9)
res=kmeans.fit_predict(datasets)

#print(dict(zip(name,res)))
#绘图
from pyecharts import Scatter3D

a=dict(zip(k,v))

def custom_formatter(params):
    return params.value[3]

d0=[datasets[i]+[name[i]] for i in range(len(name)) if res[i]==0]
d1=[datasets[i]+[name[i]] for i in range(len(name)) if res[i]==1]
d2=[datasets[i]+[name[i]] for i in range(len(name)) if res[i]==2]



scatter3D = Scatter3D("工作类别聚类", width=1200, height=600)
scatter3D.add("类别0", d0,is_visualmap=True,tooltip_formatter=custom_formatter)
scatter3D.add("类别1", d1,is_visualmap=True,tooltip_formatter=custom_formatter)
scatter3D.add("类别2", d2,is_visualmap=True,tooltip_formatter=custom_formatter,
              xaxis3d_name="管理决策",yaxis3d_name="技术",zaxis3d_name="市场营销",is_calculable=False)
scatter3D.render("工作类别聚类.html")



'''
注意实现地图可视化需要以下包：
pip install echarts-countries-pypkg
pip install echarts-china-provinces-pypkg
pip install echarts-china-cities-pypkg
'''


import csv
from pyecharts import Map

with open("data/job_skills.csv",encoding="utf-8") as file:
    datas=list(csv.DictReader(file))


country_counts=dict()
for d in datas:
    country=d['Location'].split(",")[-1].strip()
    if country in country_counts.keys():
        country_counts[country]+=1
    else:
        country_counts[country]=1

#print(country_counts)
#处理不正确的值
country_counts['United States']+=country_counts.pop('USA')
country_counts['United Arab Emirates']=country_counts.pop('Dubai - United Arab Emirates')
country_counts['China']+=country_counts.pop("Taiwan")+country_counts.pop("Hong Kong")
#print(country_counts)
country_counts_sorted=sorted(country_counts.items(),key=lambda x:x[1],reverse=True)

#绘图

from pyecharts import Map

attr = country_counts.keys()
value = country_counts.values()
map0 = Map("工作地点", width=1200, height=600)
map0.add("工作地点", attr, value, maptype="world", is_visualmap=True, visual_text_color='#000')
map0.render(path="rental.html")
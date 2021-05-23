import csv

with open("data/job_skills.csv",encoding="utf-8") as file:
    datas=list(csv.DictReader(file))

category_counts=dict()
for d in datas:
    category=d['Category'].strip()
    if category in category_counts.keys():
        category_counts[category]+=1
    else:
        category_counts[category]=1

category_counts_sorted=sorted(category_counts.items(),key=lambda x:x[1],reverse=True)

#绘图
from pyecharts import Bar

bar = Bar("工作类别",width=1200,height=600)
#绘图需要，加空项
attr=['']+[x[0] for x in category_counts_sorted]+['']
values=[0]+[x[1] for x in category_counts_sorted]+[0]
bar.add("工作类别", attr, values, xaxis_interval=0, xaxis_rotate=15, yaxis_rotate=45)
bar.render("rental.html")

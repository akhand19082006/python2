import csv
import pandas as pd
import plotly.figure_factory as pf
import plotly.graph_objects as pg
import statistics
import random
df=pd.read_csv("data.csv")
tem=df["temp"].tolist()

mean=statistics.mean(tem)
sd=statistics.stdev(tem)
median=statistics.median(tem)
mode=statistics.mode(tem)
print(mean,median,mode,sd)
fig=pf.create_distplot([tem],["Recorded Temperature"],show_hist=False)
fig.add_trace(pg.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
fig.show()
rand=[]
for i in range(0,1000):
    ran=random.randint(0,len(tem))
    value=tem[ran]
    rand.append(value)
fig=pf.create_distplot([rand],["Random Recorded temperature"])
fig.show()
n=statistics.mean(rand)
s=statistics.stdev(rand)

print(n,s)
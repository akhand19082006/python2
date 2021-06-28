import csv
import plotly.figure_factory as pf
import pandas as pd
import statistics
import plotly.graph_objects as pg
df=pd.read_csv("data2.csv")
mean=statistics.mean(df["reading score"].tolist())
standarddeviation=statistics.stdev(df["reading score"].tolist())
median=statistics.median(df["reading score"].tolist())
mode=statistics.mode(df["reading score"].tolist())
sumr=df["reading score"].tolist()
sd1start,sd1end=mean-standarddeviation,mean+standarddeviation
sd2start,sd2end=mean-(2*standarddeviation),mean+(2*standarddeviation)
sd3start,sd3end=mean-(3*standarddeviation),mean+(3*standarddeviation)
datainsd1=[result for result in sumr if result >sd1start and result <sd1end]
datainsd2=[result for result in sumr if result >sd2start and result <sd2end]
datainsd3=[result for result in sumr if result >sd3start and result <sd3end]
print(mean,"\n",standarddeviation,median,mode)
print("{}% of data lies in 1sd".format(len(datainsd1)*100.0/len(sumr)))
print("{}% of data lies in 2sd".format(len(datainsd2)*100.0/len(sumr)))
print("{}% of data lies in 3sd".format(len(datainsd3)*100.0/len(sumr)))
fig=pf.create_distplot([df["reading score"].tolist()],["Reading Score"],show_hist=False)
fig.add_trace(pg.Scatter(x=[sd1start,sd1start],y=[0,0.17],mode="lines",name="sd1start"))
fig.add_trace(pg.Scatter(x=[sd2start,sd2start],y=[0,0.17],mode="lines",name="sd2start"))
fig.add_trace(pg.Scatter(x=[sd3start,sd3start],y=[0,0.17],mode="lines",name="sd3start"))
fig.add_trace(pg.Scatter(x=[sd1end,sd1end],y=[0,0.17],mode="lines",name="sd1end"))
fig.add_trace(pg.Scatter(x=[sd2end,sd2end],y=[0,0.17],mode="lines",name="sd2end"))
fig.add_trace(pg.Scatter(x=[sd3end,sd3end],y=[0,0.17],mode="lines",name="sd3end"))
fig.add_trace(pg.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="Mean"))

fig.show()
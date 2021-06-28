import pandas as pd
import csv
import plotly.graph_objects as pg

df=pd.read_csv("data.csv")
studentdf=df.loc[df['student_id']== "TRL_987"]
print(studentdf.groupby('level')['attempt'].mean())

fig=pg.Figure(pg.Bar(x=studentdf.groupby('level')['attempt'].mean(),
y=['level 1','level 2','level 3','level 4'],
orientation='h'
))
fig.show()
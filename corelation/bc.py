import pandas as pd
import plotly.express as ps
df=pd.read_csv("bc.csv")
fig=ps.scatter(df,x="Size of TV",y="Average time spent watching TV in a week (hours)")
fig.show()
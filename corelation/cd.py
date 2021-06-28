import pandas as pd
import plotly.express as ps
df=pd.read_csv("cd.csv")
fig=ps.scatter(df,x="Coffee in ml",y="sleep in hours")
fig.show()
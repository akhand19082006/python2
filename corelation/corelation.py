import pandas as pd
import plotly.express as ps
df=pd.read_csv("ab.csv")
fig=ps.scatter(df,x="Temperature",y="Ice-cream Sales( ₹ )")
fig.show()
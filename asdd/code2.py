import plotly.figure_factory as pf
import pandas as pd
import csv
df=pd.read_csv("studentMarks.csv")
tem=df["Math_score"].tolist()
fig=pf.create_distplot([tem],["Math Score"])
fig.show()
import plotly.express as px
import csv
import numpy as np
def getDataSource(data_path):
    icecream=[]
    temperature=[]
    with open(data_path) as csv_file:
        csvreader=csv.DictReader(csv_file)
        for row in csvreader:
            temperature.append(float(row["Temperature"]))
            icecream.append(float(row["Ice-cream Sales( ₹ )"]))
    return{"x":temperature,"y":icecream}
def corelation(datasource):
    corelationvalue=np.corrcoef(datasource["x"],datasource["y"])
    print("corelation Between temperature and ice cream sale: \n",corelationvalue[0,1])
def setup():
    data_path="ab.csv"
    datasource=getDataSource(data_path)
    corelation(datasource)

setup()

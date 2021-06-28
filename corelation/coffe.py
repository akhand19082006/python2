import plotly.express as px
import csv
import numpy as np
def getDataSource(data_path):
    sleep=[]
    coffee=[]
    with open(data_path) as csv_file:
        csvreader=csv.DictReader(csv_file)
        for row in csvreader:
            sleep.append(float(row["sleep in hours"]))
            coffee.append(float(row["Coffee in ml"]))
    return{"x":coffee,"y":sleep}
def corelation(datasource):
    corelationvalue=np.corrcoef(datasource["x"],datasource["y"])
    print("corelation Between sleep  and amount of coffee: \n",corelationvalue[0,1])
def setup():
    data_path="cd.csv"
    datasource=getDataSource(data_path)
    corelation(datasource)

setup()

import plotly.express as px
import csv
import numpy as np 
def getdata(data_path):
    #icecream represents Size of TV and colddrink represents Average time spent watching TV in a week (hours)
    icecream=[]
    colddrink=[]

    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        for row in df:
            icecream.append(float(row["Size of TV"]))
            colddrink.append(float(row["Average time spent watching TV in a week (hours)"]))
    return {"x":icecream,"y":colddrink}
def findcorelation(datasource):
    corelation=np.corrcoef(datasource["x"],datasource["y"])
    print("corelation between temparature and icecream sale: ",corelation[0,1])
def setup():
    data_path="data2.csv"
    datasource=getdata(data_path)
    findcorelation(datasource)
setup()


        
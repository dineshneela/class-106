import plotly.express as px
import csv
import numpy as np 
def getdata(data_path):
    #icecream represents Marks In Percentage and colddrink represents Days Present 
    icecream=[]
    colddrink=[]

    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        for row in df:
            icecream.append(float(row["Marks In Percentage"]))
            colddrink.append(float(row["Days Present"]))
    return {"x":icecream,"y":colddrink}
def findcorelation(datasource):
    corelation=np.corrcoef(datasource["x"],datasource["y"])
    print("corelation between temparature and icecream sale: ",corelation[0,1])
def setup():
    data_path="data3.csv"
    datasource=getdata(data_path)
    findcorelation(datasource)
setup()


        
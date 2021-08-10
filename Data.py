import csv
import numpy as np

def getdatasources(data_path):
    marks=[]
    days=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return {"x":marks,"y":days}

def findcorelation(datasources):
    corelation=np.corrcoef(datasources["x"],datasources["y"])
    print("corelation between marks and days persent:",corelation[0,1] )

def setup():
    data_path="Data.csv"
    dataSource=getdatasources(data_path)
    findcorelation(dataSource)

setup()
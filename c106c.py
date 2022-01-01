import plotly.express as px
import csv 
import numpy as np
def getdatasource(datapath):
    coffee=[]
    sleep=[]
    with open(datapath)as f:
        csvreader=csv.DictReader(f)
        for row in csvreader:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return {'x':coffee,'y':sleep}

def findcorelation(datasource):
    corelation=np.corrcoef(datasource['x'],datasource['y'])
    print('corelation between coffee and sleep sales is ',corelation[0,1])

def setup():
    datapath='coffeevssleep.csv'
    datasource=getdatasource(datapath)
    findcorelation(datasource)

setup()    
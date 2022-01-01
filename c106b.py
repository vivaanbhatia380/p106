import plotly.express as px
import csv 
import numpy as np
def getdatasource(datapath):
    icecreamsales=[]
    temperature=[]
    with open(datapath)as f:
        csvreader=csv.DictReader(f)
        for row in csvreader:
            icecreamsales.append(float(row['Ice-cream']))
            temperature.append(float(row['Temperature']))
    return {'x':icecreamsales,'y':temperature}

def findcorelation(datasource):
    corelation=np.corrcoef(datasource['x'],datasource['y'])
    print('corelation between temperature and icecream sales is ',corelation[0,1])

def setup():
    datapath='Ice-CreamvsTemperature.csv'
    datasource=getdatasource(datapath)
    findcorelation(datasource)

setup()    
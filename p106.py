import plotly.express as px
import csv 
import numpy as np

def plotfigure(datapath):
    with open (datapath)as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x='Days Present',y='Marks In Percentage')
        fig.show()
def getdatasource(datapath):
    studentmarks=[]
    pdays=[]
    with open(datapath)as f:
        csvreader=csv.DictReader(f)
        for row in csvreader:
            studentmarks.append(float(row['Marks In Percentage']))
            pdays.append(float(row['Days Present']))
    return {'x':studentmarks,'y':pdays}

def findcorelation(datasource):
    corelation=np.corrcoef(datasource['x'],datasource['y'])
    print('corelation between marks and present days is ',corelation[0,1])

def setup():
    datapath='StudentMarksvsDaysPresent.csv'
    datasource=getdatasource(datapath)
    findcorelation(datasource)
    plotfigure(datapath)

setup()    
import plotly.express as px
import csv 
with open('Ice-CreamvsTemperature.csv')as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x='Temperature',y='Ice-cream')
    fig.show()
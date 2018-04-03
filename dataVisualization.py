import MySQLdb
import pandas as pd

import plotly.offline as py
from plotly.graph_objs import *



conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="world")
cursor = conn.cursor()
cursor.execute('select Name, Continent, Population, LifeExpectancy, GNP from Country')
rows = cursor.fetchall()

for i in rows:
    print(i)


df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'Name', 1: 'Continent', 2: 'Population', 3: 'LifeExpectancy', 4:'GNP'}, inplace=True)

print(df)


 
trace1 = Scatter(
     x=df['Name'],
     y=df['Population'],
    
     mode='markers'
)
layout = Layout(
     xaxis=XAxis( title='Conutry Name' ),
     yaxis=YAxis( type='log', title='Population' )
)
data = Data([trace1])
fig = Figure(data=data, layout=layout)
py.offline.plot(data, filename='file.html')

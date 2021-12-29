import csv
from numpy.lib.function_base import corrcoef
from pandas.io.parsers import read_csv
import plotly_express as px
import numpy as np
import pandas as pd




marks=[]
daysPresent=[]

with open("marks.csv") as f:
    reader=csv.DictReader(f)
    for row in reader:
        marks.append(float(row["Marks In Percentage"]))
        daysPresent.append(float(row["Days Present"]))
correlation=np.corrcoef(marks,daysPresent)

cor=correlation

#df=pd.read_csv("marks.csv")
#fig=px.scatter(df,x="Marks In Percentage",y="Days Present",text=cor)
#fig.show()


print("Correlation between the Marks Percentage and Days Present is :- \n--->",correlation[0,1])


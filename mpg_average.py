import pandas as pd
import math

df=pd.read_csv('cars.csv')

mpg_column=df['MPG'].tail(406)

mpg_list=[]
for i in mpg_column:
     mpg_list.append(float(i))

mpg_avg=sum(mpg_list)/len(mpg_list)
mpg_avg=round(mpg_avg,3)

print("The average of all cars MPG is",mpg_avg)
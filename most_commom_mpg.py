import pandas as pd 

df=pd.read_csv('cars.csv')

mpg_clm=df["MPG"]
mpg_clm=mpg_clm.tail(406)

mpg_list=[]

for i in mpg_clm:
     mpg_list.append(float(i))

commom_mpg=max(set(mpg_list),key=mpg_list.count)

print("Most common MPG of all cars is",commom_mpg)
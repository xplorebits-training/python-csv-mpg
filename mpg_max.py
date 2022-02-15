import pandas as pd

df=pd.read_csv('cars.csv')

mpg_clm=df["MPG"]
mpg_clm=mpg_clm.tail(406)

mpg_list=[]

for i in mpg_clm:
     mpg_list.append(float(i))

mpg_max=max(mpg_list)

mpg_max_index=mpg_list.index(mpg_max)+1

print("Car details with maximum MPG are")
print(df.loc[int(mpg_max_index)])
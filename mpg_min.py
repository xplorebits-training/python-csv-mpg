import pandas as pd 

df=pd.read_csv('cars.csv')

mpg_column=df["MPG"].tail(406)
cars_column=df['Car']

mpg_list=[]
for i in mpg_column:
     mpg_list.append(float(i))

cars_list=[]

for i in cars_column:
     cars_list.append(i)

car_0_mpg=[]
count=1
for i in mpg_list:
     if(i==0.0):
          car_0_mpg.append(cars_list[count])
     count+=1

car_0_mpg=sorted(car_0_mpg)

car_min_mpg=car_0_mpg[0]
car_min_mpg=cars_list.index(car_min_mpg)

print("Car details with minimum MPG are")
print(df.loc[car_min_mpg])
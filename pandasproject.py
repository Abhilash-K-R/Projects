#A project that involves Data cleaning and visualization 
#using pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
#reading the csv file
df=pd.read_csv('data.csv')
print(df)

print(' ')

#Data cleaning or cleaning the missing values
cleaned_data=df.dropna()

print(cleaned_data)

print(' ')

#print few records from the cleaned data
print(cleaned_data.head())

print(' ')
#info or cleaned data
print(cleaned_data.info())


print(' ')
#Descriptive statistics...

print('Descriptive statistics: ')
print(cleaned_data.describe())


#Data visualization using matplotlib 
plt.figure(figsize=(8,6))
plt.hist(cleaned_data['Age'],bins=6,color='red',edgecolor='black',
         alpha=0.5)
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

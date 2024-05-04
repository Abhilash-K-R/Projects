#A mini project to analyze student marks data using numpy and matplotlib.
# Finding the no.of passed students
#Finding Pass percentage
# Finding Descriptive statistics.

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42) #to reproducability
marks=np.random.randint(0,101,size=1000)
print('Student marks: ',marks)

#Finding Descriptive statistics
mean=np.mean(marks)
median=np.median(marks)
std=np.std(marks)
max=np.max(marks)
min=np.min(marks)

print(' ')
print('Descriptive statistics: ')
print('Mean is: ',mean)
print('Median is: ',median)
print('Standard Deviation is: ',std)
print('Max val is: ',max)
print('Min val is: ',min)

#no.of students passed
passed_students=np.sum(marks>=50)
print('Passed students: ',passed_students)

#no.of pass percentage
pass_percentage=(passed_students/len(marks))*100
print('Pass percentage of students: ',pass_percentage,' %')



#Data Visualization of marks and count
#using Histogram
plt.figure(figsize=(8,6))
plt.hist(marks,bins=7,color='green',edgecolor='yellow',alpha=0.5)
plt.title('Student Marks and count of Passed students')
plt.xlabel('Marks')
plt.ylabel('Count')
plt.grid(True)
plt.show()

print('     ')
print('     ')
#Data using pie chart
bins=[0,20,40,60,80,100]

frequency,a=np.histogram(marks,bins=bins)

labels=['0-20','21-40','41-60','61-80','81-100']

plt.figure(figsize=(8,6))
plt.pie(frequency,labels=labels,autopct='%1.1f%%',
        colors=['Gold','yellowgreen','lightskyblue','lightcoral','lightpink'],startangle=140)
plt.title('Student Marks')
plt.axis('equal')
plt.show(

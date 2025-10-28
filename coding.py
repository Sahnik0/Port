#Create a dataframe with 10 students name,marks of three courses-python, software engineering,network and attendance percentage. Perform the following tasks on the dataframe:
#1. Print the students name whose average marks>90
#2. Print the students name whose attendance<75%
#3. Print the name of top 3 students whose average>90 and attendance>75
#4. Find correlation among average score and attendance

import pandas as pd
df=pd.read_csv("students.csv")
df['average']=(df['python']+df['software engineering']+df['network'])/3
print("Students with average marks > 90:")
print(df[df['average']>90]['name'])
print("\nStudents with attendance < 75%:")
print(df[df['attendance']<75]['name'])
top_students=df[(df['average']>90) & (df['attendance']>75)].nlargest(3,'average')
print("\nTop 3 students with average > 90 and attendance > 75%:")
print(top_students['name'])
correlation=df['average'].corr(df['attendance'])
print("\nCorrelation between average score and attendance:")
print(correlation)
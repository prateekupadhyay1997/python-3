#this code represents deep copy in which
#the changes made in the new variable will
# not be reflected into the original variable
# importing pandas module 
import pandas as pd 

# creating sample series 
data = pd.Series(['a', 'b', 'c', 'd']) 

# creating copy of series 
new = data.copy() 

# assigning new values 
new[1]='Changed value'

# printing data 
print(new) 
print(data) 

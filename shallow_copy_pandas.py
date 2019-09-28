#this code is for representing a shallow copy
#in which both the variables will refer to the same
#object and any changes made to the copy variable
#will also be reflected into the original variable

# importing pandas module 
import pandas as pd 

# creating sample series 
data = pd.Series(['a', 'b', 'c', 'd']) 

# creating copy of series 
new = data 

# assigning new values 
new[1]='Changed value'

# printing data 
print(new) 
print(data) 

import pandas as pd
import scipy
import scipy.stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()
print(data)
data = [i.split(',') for i in data]
print(data)

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)
print("__________________________________________________")
print(df)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print("__________________________________________________")
print("The mean for the Alcohol is "+str(df['Alcohol'].mean()))
print("The median for the Alcohol is "+str(df['Alcohol'].median()))
print("The mode for the Alcohol is "+str(scipy.stats.mode(df['Alcohol'])[0][0]))
print("The range for the Alcohol is "+str(max(df['Alcohol']) - min(df['Alcohol'])))
print("The standard deivation for the Alcohol is "+str(df['Alcohol'].std() ))
print("The variance for the Alcohol is "+str(df['Alcohol'].var()))
print("__________________________________________________")
print("The mean for the Tobacco dataset is "+str(df['Tobacco'].mean()))
print("The median for the Tobacco dataset is "+str(df['Tobacco'].mean()))
print("The mode for the Tobacco dataset is "+str(scipy.stats.mode(df['Tobacco'])[0][0]))
print("The range for the Tobacco is "+str(max(df['Tobacco']) - min(df['Tobacco'])))
print("The standard deivation for the Tobacco is "+str(df['Tobacco'].std() ))
print("The variance for the Tobacco is "+str(df['Tobacco'].var()))
print("__________________________________________________")

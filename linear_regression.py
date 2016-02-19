#2.3.2 Cleaning data

import pandas as pd
import matplotlib.pyplot as plt
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

print(loansData['Interest.Rate'][0:5])

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate

print(loansData['Interest.Rate'][0:5])
print('_____________________________')
print(loansData['Loan.Length'][0:5])

cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
loansData['Loan.Length'] = cleanLoanLength
print(loansData['Loan.Length'][0:5])
print('_____________________________')

print(loansData['FICO.Range'][0:5])
loansData['FICO.Score'] = loansData['FICO.Range'].astype('string')
loansData['FICO.Score'] = map(lambda x: int(x.split("-")[0]), loansData['FICO.Score']) 

print(loansData['FICO.Score'][0:5])
print('_____________________________')

plt.figure()
p = loansData['FICO.Score'].hist()
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
#plt.show()

#2.3.3 Linear Regression Analysis

import numpy as np
import pandas as pd
import statsmodels.api as sm

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print(f.summary())




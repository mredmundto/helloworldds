import pandas as pd
#from scipy import stats
#import collections
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
cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFICORange = cleanFICORange.map(lambda x: [int(n) for n in x])
loansData['FICO.Range'] = cleanFICORange
print(loansData['FICO.Range'][0:5])
print('_____________________________')

plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()



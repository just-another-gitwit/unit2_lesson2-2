#import modules
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

#load data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#remove null value rows
loansData.dropna(inplace=True)

#generate box plot
loansData.boxplot(column='Amount.Requested')
plt.savefig("AmountRequestedboxplot.png")

#generate histogram
loansData.hist(column='Amount.Requested')
plt.savefig("AmountRequestedhistogram.png")

#generate qq-plot
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("AmountRequestedqqplot.png")

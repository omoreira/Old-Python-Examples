# 2samplepaired_braindata.py:  
import pandas
from scipy import stats
import numpy
# reading data file
data = pandas.read_csv('http://www.scipy-lectures.org/_downloads/brain_size.csv', sep=';', na_values=".")
#Defining significance level 
alpha=0.05
#Perfoming Barlett's Test. This tests whether the populations variances are equal
t, p = stats.bartlett(data['FSIQ'], data['PIQ']) 
print 'barlett test statistic is', t, 'and p-value', p
# Perfoming decision rule test rejects or fails to reject null hypothesis based on p-value and significance level 
if p <= alpha:
	print 'p-value is too small, null hypothesis is rejected. Variances of the data sets are not equal'
else:
	print 'P-value is greater than significance level',alpha,', Barlett test fails to reject the null hypothesis. Variances are similar'
#Performing Levene's Test. This tests whether the populations are equal
t, p = stats.levene(data['FSIQ'], data['PIQ']) 
print 'Levene test statistic is', t, 'and p-value', p
# Perfoming decision rule test rejects or fails to reject null hypothesis based on p-value and significance level 
if p <= alpha:
	print 'p-value is too small, null hypothesis is rejected. Variances of the data sets are not equal'
else:
	print 'P-value is greater than significance level',alpha,', Levene test fails to reject the null hypothesis. Variances are similar'
#Performing Paired Samples t-test. 
# Null Hypothesis: Mean Full Scale IQ (FSIQ) and Mean Performance IQ (PIQ), measured on the same individuals, are equal. " 
t, p=stats.ttest_rel(data['FSIQ'], data['PIQ'])  
print 'Paired  t- test statistic is', t, 'and p-value', p
#Calculation of difference between mean point estimates:
diffmean=abs(numpy.mean(data['FSIQ']) - numpy.mean(data['PIQ']))
# Perfoming decision rule test rejects or fails to reject null hypothesis based on p-value and significance level 
if p <= alpha:
	print 'p-value is too small, null hypothesis is rejected. FSIQ and PIQ  are very difference. The difference between FSIQ and PIQ means  (point estimates) is',diffmean 
else:
	print 'P-value is greater than significance level',alpha,', Paired t-test fails to reject the null hypothesis. Mean FSIQ and Mean PIQ  are similar'
	
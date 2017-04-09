# 1samp_ttest_1.py : 
#This an example based on http://www.scipy-lectures.org/packages/statistics/index.html#student-s-t-test-the-simplest-statistical-test 
# Dataset Available at: http://www.scipy-lectures.org/_downloads/brain_size.csv 
# See: https://www.gabormelli.com/RKB/One-Sample_t-Test_System
# This performs One-Sample t-Test, for the Verbal IQ (VIQ) dataset of Null Hypotheses: 
#1. Verbal IQ mean value is 0
#2. Verbal IQ mean value is 115
#3. Verbal IQ mean value is 112
import pandas
from scipy import stats
# reading data file
data = pandas.read_csv('http://www.scipy-lectures.org/_downloads/brain_size.csv', sep=';', na_values=".")
#Null Hypotheses values
NH=[0,115,200]
#Significance level
alpha = 0.05
# One-Sample t-Test
for i in range(3):
	print '___________'
	# Null Hypothesis statement 
	print 'Null Hypotesis: VIQ population mean value is', NH[i]
	# One-Sample t-Statistic calculation
	t,p=stats.ttest_1samp(data['VIQ'], NH[i])
	print 'one-sample t-statistic value:', t , 'p-value:', p
	#Decision rule: p-value
	if p < alpha:
		print 'p-value is too small, null hypothesis is rejected. VIQ population mean value is NOT',NH[i]
	else:
		print 'P-value is greater than significance level',alpha,', test fails to reject the null hypothesis. VIQ population mean value can be', NH[i]
	
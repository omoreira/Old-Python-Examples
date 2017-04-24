# welchtestexample.py 
#This program perform the following tests: 
# A) Barlett's and Levene's Test for testing homogeinity of variances;
# B) and Welch's Test (Difference between Means test)
# This is based on the dataset available at http://libguides.library.kent.edu/ld.php?content_id=11205378
# This example test the null hypothesis that Athelete (group1) and Nonathelete (group 2) students 
# mile run time are similar  
from scipy import stats
import pandas
import numpy
data = pandas.read_csv('http://libguides.library.kent.edu/ld.php?content_id=11205378', sep=',', na_values=".")
#Defining mile run time for datasets: "Athelete"  and "Nonathelete"  
athelete = data[data['Athlete'] == 1]['MileMinDur']
nonathelete = data[data['Athlete'] == 0]['MileMinDur']
# Converting dataset from  hh:mm:ss format to a numerical number: running time in minutes
athelete=athelete.astype(str).reshape(athelete.size,1)
nonathelete=nonathelete.astype(str).reshape(nonathelete.size,1)
athelete=athelete[numpy.where(athelete!=[' '])]
nonathelete=nonathelete[numpy.where(nonathelete!=[' '])]
for i in range(numpy.shape(athelete)[0]) :
	h,m,s=athelete[i].split(':')
	athelete[i]=int(h)*60+int(m)+(int(s)/60.)
for j in range(numpy.shape(nonathelete)[0]) :
	h,m,s=nonathelete[j].split(':')
	nonathelete[j]=int(h)*60+int(m)+(int(s)/60.)	
#Defining significance level 
alpha=0.05
#Perfoming Barlett's Test. This tests whether the populations variances are equal
t, p = stats.bartlett(athelete,nonathelete)
print 'barlett test statistic is', t, 'and p-value', p
# Perfoming decision rule test rejects or fails to reject null hypothesis based on p-value and significance level 
if p <= alpha:
	print 'p-value is too small, null hypothesis is rejected. Variances of the data sets are not equal'
else:
	print 'P-value is greater than significance level',alpha,', Barlett test fails to reject the null hypothesis. Variances are similar'
#Performing Levene's Test. This tests whether the populations are equal
t, p = stats.levene(athelete,nonathelete)
print 'Levene test statistic is', t, 'and p-value', p
# Perfoming decision rule test rejects or fails to reject null hypothesis based on p-value and significance level 
if p <= alpha:
	print 'p-value is too small, null hypothesis is rejected. Variances of the data sets are not equal'
else:
	print 'P-value is greater than significance level',alpha,', Levene test fails to reject the null hypothesis. Variances are similar'
#Performing Welch's Test. This test whether population means are equal
t, p=stats.ttest_ind(athelete,nonathelete, equal_var = False)
print 'Welchs test statistic is', t, 'and p-value', p
#Calculation of difference between mean point estimates:
diffmean=abs(numpy.mean(athelete) - numpy.mean(nonathelete))
# Perfoming decision rule test rejects or fails to reject null hypothesis based on p-value and significance level 
if p <= alpha:
	print 'p-value is too small, null hypothesis is rejected. Athelete and nonathelete students mean mile run times  are very difference. The difference between mean mile run times (point estimates) is',int(diffmean),'minutes and', int((diffmean -int(diffmean))/6.), 'seconds'  
else:
	print 'P-value is greater than significance level',alpha,', Welchs test fails to reject the null hypothesis.  Athelete and nonathelete students mean mile run times are similar'

# Welch's Test example

from scipy import stats
import pandas
import numpy
data2 = pandas.read_csv('http://libguides.library.kent.edu/ld.php?content_id=11205378', sep=',', na_values=".")
athelete = data2[data2['Athlete'] == 1]['MileMinDur']
nonathelete = data2[data2['Athlete'] == 0]['MileMinDur']
# Convert dataset from  hh:mm:ss format to a numerical number miles seconds
xdata1=athelete.astype(str).reshape(athelete.size,1)
xdata2=nonathelete.astype(str).reshape(nonathelete.size,1)
xdata1=xdata1[numpy.where(xdata1!=[' '])]
xdata2=xdata2[numpy.where(xdata2!=[' '])]
for i in range(numpy.shape(xdata1)[0]) :
	h,m,s=xdata1[i].split(':')
	xdata1[i]=int(h)*60+int(m)+(int(s)/60.)
for j in range(numpy.shape(xdata2)[0]) :
	h,m,s=xdata2[j].split(':')
	xdata2[j]=int(h)*60+int(m)+(int(s)/60.)	
#Defining significance level 
alpha=0.05
#Barlett's test
t, p = stats.bartlett(xdata1,xdata2)
print 'barlett test statistic is', t, 'and p-value', p
if p <= alpha:
	print 'p-value is too small, null hypothesis is rejected. Variances of the data sets are not equal'
else:
	print 'P-value is greater than significance level',alpha,', Barlett test fails to reject the null hypothesis. Variances are similar'
#Levene's Test
t, p = stats.levene(xdata1,xdata2)
print 'Levene test statistic is', t, 'and p-value', p
if p <= alpha:
	print 'p-value is too small, null hypothesis is rejected. Variances of the data sets are not equal'
else:
	print 'P-value is greater than significance level',alpha,', Levene test fails to reject the null hypothesis. Variances are similar'
#Welch's Test
diffmean=abs(numpy.mean(xdata1) - numpy.mean(xdata2))
t, p=stats.ttest_ind(xdata1,xdata2, equal_var = False)
print 'Welchs test statistic is', t, 'and p-value', p
if p <= alpha:
	print 'p-value is too small, null hypothesis is rejected. Populations mean are very difference. The difference between mean point estimates is',int(diffmean),'minutes and', int((diffmean -int(diffmean))/6.), 'seconds'  
else:
	print 'P-value is greater than significance level',alpha,', Welchs test fails to reject the null hypothesis.  Population means are very similar'

#10 Fold Boston Data and Lasso Regression
# Based on http://facweb.cs.depaul.edu/mobasher/classes/CSC478/Notes/IPython%20Notebook%20-%20Regression.html
from sklearn.cross_validation import KFold
from sklearn.linear_model import Lasso
import numpy as np
import pylab as pl
from sklearn.datasets import load_boston
#Loading boston datasets 
boston = load_boston()
# Adding a column of 1s for x0 (Regression Design Matrix)
x = np.array([np.concatenate((v,[1])) for v in boston.data])
y = boston.target
# Create linear regression object with a lasso coefficient 0.3
lasso = Lasso(fit_intercept=True, alpha=0.5)
# Train the model using the training set
lasso.fit(x,y)
# predictions p = np.array([lasso.predict(xi) for xi in x])
p = lasso.predict(x)
#plotting real vs predicted data
pl.plot(p, y,'ro')
pl.xlabel('predicted')
pl.title('Lasso Regression, alpha=0.5')
pl.ylabel('real')
pl.grid(True)
pl.show()
#vector of errors
err = p-y
# Dot product of error vector is sum of squared errors
total_error = np.dot(err,err)
#RMSE on training data
rmse_train = np.sqrt(total_error/len(p))
# Compute RMSE using 10-fold x-validation
kf = KFold(len(x), n_folds=10)
xval_err = 0
for train,test in kf:
    lasso.fit(x[train],y[train])
    p = lasso.predict(x[test])
    e = p-y[test]
    xval_err += np.dot(e,e)
rmse_10cv = np.sqrt(xval_err/len(x))
print('Method: Lasso Regression')
print('RMSE on training: %.4f' %rmse_train)
print('RMSE on 10-fold CV: %.4f' %rmse_10cv)


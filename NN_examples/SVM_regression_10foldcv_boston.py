# SVM Regression 10-fold CV example using Boston dataset.
import numpy as np
import matplotlib.pyplot as pl
from sklearn import svm 
from sklearn import datasets
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.model_selection import cross_val_predict
from sklearn import cross_validation
# ###########################################
# Load data
boston = datasets.load_boston()
# Creating Regression Design Matrix 
x = boston.data
# Creating target dataset
y = boston.target
x_train, x_test, y_train, y_test= cross_validation.train_test_split(x, y, test_size=0.45)
# ##########################
# Fit regression model
n_fig=0
for name, svm_reg in [
        ('Linear Support Vector Regression ', svm.LinearSVR()), ('Nu Support Vector Regression', svm.NuSVR()), ('Epsilon-Support Vector Regression', svm.SVR())
        ]:
    regressormodel=svm_reg.fit(x_train,y_train)
    # Y predicted values
    yp =svm_reg.predict(x_test)
    #RMSE
    rmse =np.sqrt(mean_squared_error(y_test,yp))
    #Calculation 10-Fold CV
    yp_cv = cross_val_predict(regressormodel, x_test, y_test, cv=10)
    rmsecv=np.sqrt(mean_squared_error(y_test,yp_cv))
    print('Method: %s' %name)
    print('RMSE on the train data: %.4f' %rmse)
    print('RMSE on 10-fold CV: %.4f' %rmsecv)    
    n_fig=n_fig+1
    pl.figure(n_fig)
    pl.plot(yp, y_test,'ro')
    pl.plot(yp_cv, y_test,'bo', alpha=0.25, label='10-folds CV')
    pl.xlabel('predicted')
    pl.title('Method: %s' %name)
    pl.ylabel('real')
    pl.grid(True)
    pl.show()
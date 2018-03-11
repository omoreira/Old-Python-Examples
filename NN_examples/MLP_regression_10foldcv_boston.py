# MLP Regression 10-fold CV example using Boston dataset.
import numpy as np
import matplotlib.pyplot as pl
from sklearn import neural_network 
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
#x_train, x_test, y_train, y_test= cross_validation.train_test_split(x, y, test_size=0.2, random_state=42)
# ######################################################################
# Fit regression model
n_fig=0
for name, nn_unit in [
        ('MLP using ReLU', neural_network.MLPRegressor(activation='relu', solver='lbfgs')), ('MLP using Logistic Neurons', neural_network.MLPRegressor(activation='logistic')), ('MLP using TanH Neurons', neural_network.MLPRegressor(activation='tanh',solver='lbfgs'))
        ]:
    regressormodel=nn_unit.fit(x,y)
    # Y predicted values
    yp =nn_unit.predict(x)
    rmse =np.sqrt(mean_squared_error(y,yp))
    #Calculation 10-Fold CV
    yp_cv = cross_val_predict(regressormodel, x, y, cv=10)
    rmsecv=np.sqrt(mean_squared_error(y,yp_cv))
    print('Method: %s' %name)
    print('RMSE on the data: %.4f' %rmse)
    print('RMSE on 10-fold CV: %.4f' %rmsecv)
    n_fig=n_fig+1
    pl.figure(n_fig)
    pl.plot(yp, y,'ro')
    pl.plot(yp_cv, y,'bo', alpha=0.25, label='10-folds CV')
    pl.xlabel('predicted')
    pl.title('Method: %s' %name)
    pl.ylabel('real')
    pl.grid(True)
    pl.show()

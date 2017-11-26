# Regression Trees 10-fold CV
import numpy as np
import matplotlib.pyplot as plt
from sklearn import ensemble
from sklearn import datasets
from sklearn import tree
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.model_selection import cross_val_predict
#from sklearn import cross_validation
# #############################################################################
# Load data
boston = datasets.load_boston()
# Creating Regression Design Matrix 
x = boston.data
# Creating target dataset
y = boston.target
#x_train, x_test, y_train, y_test= cross_validation.train_test_split(x, y, test_size=0.2, random_state=42)
# #############################################################################
# Fit regression model
for name,met in [
        ('Gradient Boosting Regressor', ensemble.GradientBoostingRegressor(n_estimators= 500, max_depth=4, min_samples_split=2, learning_rate= 0.01, loss= 'ls')),
        ('Random Forest Regressor', ensemble.RandomForestRegressor(n_estimators=500, max_depth= 4, min_samples_split= 2)),
        ('Extra Trees Regressor', ensemble.ExtraTreesRegressor(n_estimators= 500, max_depth=4, min_samples_split=2)),
        ('Bagging Regressor', ensemble.BaggingRegressor(n_estimators= 500)),
        ('AdaBoost Regressor', ensemble.AdaBoostRegressor(n_estimators= 500, learning_rate= 0.01, loss= 'linear')),
        ('Decision Tree Regressor', tree.DecisionTreeRegressor(max_depth= 4, min_samples_split= 2))]:
    regressormodel=met.fit(x,y)
    # Y predicted values
    yp =met.predict(x)
    rmse =np.sqrt(mean_squared_error(y,yp))
    #Calculation 10-Fold CV
    yp_cv = cross_val_predict(regressormodel, x, y, cv=10)
    rmsecv=np.sqrt(mean_squared_error(y,yp_cv))
    print('Method: %s' %name)
    print('RMSE on the data: %.4f' %rmse)
    print('RMSE on 10-fold CV: %.4f' %rmsecv)



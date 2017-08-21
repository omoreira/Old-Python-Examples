import numpy as np
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
# Generating data
xi = np.array([i*np.pi/180 for i in range(60,300,4)])
np.random.seed(10)
n_samples=len(xi)
yi = np.sin(xi) + np.random.normal(0,0.15,n_samples)
# generating regression coefficients, betas
n_features=5
np.random.seed(0)
beta=np.random.randn(n_features)
#Calculating Predictors, X*beta
xij=np.vstack((np.ones(n_samples),xi))
for j in range(n_features-2):
	xij=np.vstack((xij, xi**(j+2)))
predictors = np.transpose(xij)*beta
#Generating regularization parameters, alphas
alpha_ridge = [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2, 1, 5, 10, 20]
n_alphas=np.size(alpha_ridge)
#Ridge Regression
for k in range(n_alphas):
    ridgereg = Ridge(alpha=alpha_ridge[k])
    ridgereg.fit(predictors,yi)
    y_pred = ridgereg.predict(predictors)
    plt.plot(xi,y_pred,'-')
plt.plot(xi,yi,'bo')
plt.title('Ridge Regression')
plt.xlabel('$x$',size=24)
plt.ylabel('$y$',size=24)
plt.legend()
plt.show()
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
f = np.poly1d([5, 1])
x = np.linspace(0, 10, 30)
y = f(x) + 6*np.random.normal(size=len(x))
xn = np.linspace(0, 10, 200)
a = np.vstack([x, np.ones(len(x))]).T
cf=np.linalg.lstsq(a, y)[0]
print 'Regression Coefficients', cf
yn=cf[1]+cf[0]*xn
plt.plot(x,y,'bo',label='data')
plt.plot(xn,yn,'g-',label='lsq')
plt.xlabel('$x$',size=24)
plt.ylabel('$y$',size=24)
plt.legend()
plt.show()


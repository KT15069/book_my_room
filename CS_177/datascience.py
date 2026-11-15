
def func(x):
    return slope*x + intercept

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

y=np.array([50,52,48,60,59,70,65,60,50])
x=np.array([2010,2011,2012,2013,2014,2015,2016,2017,2018])
plt.scatter(x,y,color="#FFBF00")

slope,intercept,r,p,std_err=stats.linregress(x,y)
print(f"Slope: {slope}\nIntercept: {intercept},\nR-value: {r},\np-value: {p},\nStandardError: {std_err}")

fx=slope*x + intercept
print(f"Mean:{np.mean(y)}, Median:{np.median(y)}, Mode-object:{stats.mode(y)}\nMode:{stats.mode(y).mode}, ModeCount:{stats.mode(y).count}")
plt.plot(x,fx, color="pink")

mapx=map(func,x)
print(np.array(list(mapx)))
print(f"Standard Deviation(population): {np.std(x)}, Std Sample:{np.std(x,ddof=1)} ")
plt.show()


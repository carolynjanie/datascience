# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from statistics import mean
import numpy as np
from matplotlib import pyplot as plt

xs = np.array([1,2,3,4,5,6], dtype=np.float64)
ys=np.array( [4,5,7,8,9,12] ,dtype=np.float64)
plt.plot(xs,ys)
plt.show()

def best_fit_slope_and_intercept(xs,ys):
    m=  ( (mean(xs)*mean(ys)-mean(xs*ys)) /
                ((mean(xs))*( mean(xs))-(mean(xs*xs))))
                
    b =mean(ys)-m*mean(xs)
    return  m,b    
def squared_error(ys_orig,ys_line):
    return sum((ys_line-ys_orig)**2)
def coefficient_of_determination(ys_orig,ys_line):
    y_mean_line=[mean(ys_orig)for y in ys_orig]
    squared_error_regre=squared_error(ys_orig,ys_line)
    squared_error_y_mean=squared_error(ys_orig,y_mean_line)
    return (squared_error_regre /  squared_error_y_mean)

    
    
    
    
                

m ,b =best_fit_slope_and_intercept(xs,ys) 

regression_line=[(m*x)+b for x in xs]
predict_x=8.9
predict_y=(m*predict_x)+b
r_squared=coefficient_of_determination(ys,regression_line)
print(r_squared)

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y,color="red")
plt.plot(xs,regression_line)
plt.show
   
    
 
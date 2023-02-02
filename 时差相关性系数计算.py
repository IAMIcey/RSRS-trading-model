# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:15:47 2021

@author: dunhe
"""

def TimeDifference(base_index,testing_index):
    import matplotlib.pyplot as plt
    import numpy as np
    import math
    import pandas as pd
    import preprocessing as pre
    pd_ratio = pd.DataFrame(pre.prepocessing(base_index).tolist(),columns = ["base_index"])
    pd_ratio1 = pd.DataFrame(pre.prepocessing(testing_index).tolist(),columns = ['testing_index'])

    sourse = pd_ratio.join(pd_ratio1)
    sourse = sourse.dropna()

    x = sourse['base_index'].tolist()
    y = sourse['testing_index'].tolist()

    x_mean = np.mean(x)
    y_mean = np.mean(y)
    rel = []
    a = b= c = d = 0

    for l in range(-12,13):
        asum = bsum = csum = ksum = 0
        if l >= 0:
            for t in range(0,len(sourse)-l):
                a = (x[t+l] - x_mean)*(y[t]-y_mean)
        
                b = pow((x[t+l] - x_mean),2)
                C = pow((y[t] - y_mean),2)        
                asum = a + asum
                bsum = b + bsum
                csum = c + csum
          
        else:
           ll = -l
           for t in range(ll,len(sourse)):
               a = (x[t+l] - x_mean)*(y[t] - y_mean)
               b = pow((x[t+l] - x_mean),2)
               c = pow((y[t] - y_mean),2)   
               asum = a + asum
               bsum = b + bsum
               csum = c + csum
           
        d = np.sqrt(bsum*csum)
    
        if asum == d ==0:
            r = 0
        else:
                r = asum/d
                rl = abs(r)
                rel.append(rl)
        if rl == max(rel):
            time = abs(l)
    print("时差相关系数为:",rl)
    print("时差相关性领先月数:",time)
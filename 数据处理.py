# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 13:30:48 2021

@author: dunhe
"""

def prepocessing(df):# df 为相应指标的环比DATAFRAME
    import matplotlib.pyplot as plt
    import statsmodels.api as sm
    import numpy as np
    import math
    from WindPy import w
    import pandas as pd
    CPI_data1 = w.edb("M0000705", "2002-01-01", "2021-07-15","Fill=Previous")
    CPI_data1_df = pd.DataFrame(CPI_data1.Data,columns = CPI_data1.Times,index= CPI_data1.Codes).T
    CPI_data1_df.columns = ["基准"]
    base_df = CPI_data1_df
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False
    PATH = 'Users\dunhe\Desktop\x13as.exe'
    df = df + 1
    df = df.cumprod()
    df = base_df.join(df)
    df = df.fillna(method = "ffill")
    df = df.fillna(method = "bfill")
    result = sm.tsa.x13_arima_analysis(df[df.columns[1]])
    result.plot()
    result.trend = result.trend.dropna()
    cycle, trend = sm.tsa.filters.hpfilter(result.trend, lamb = 129600)
    cycle = cycle/10
    cycle = cycle + 1
    dcycle = cycle.pct_change(12)
    dcycle = dcycle.dropna()
    fig,axes = plt.subplots()
    dcycle.plot(subplots = True, title = "指标预处理后同比图像")
    return dcycle

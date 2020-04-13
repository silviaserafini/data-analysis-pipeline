import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def plotTime(df_analysis):
    df_analysis["2MONTHS_BINS"] = pd.cut(df_analysis.MONTH, bins=[0,2,4,6,8,10,12],
                     labels=['01-02','03-04','05-06','07-08','09-10','11-12'])
    res = df_analysis.groupby("2MONTHS_BINS").agg({"ARR_DELAY": "mean","DEP_DELAY":"mean"})
    res1=res.plot.bar()
    fig=res1.get_figure()
    fig.subplots_adjust(bottom=0.2)
    plt.title('Avarage dealays [2 months bins]')
    plt.show()
    fig.savefig('SRC/plot.jpg')
    res.to_csv("SRC/2monthsbins.csv")
    
    return res
    
def plotAirline(df1):
    res=df1.groupby("AIRLINE_NAME").agg({"ARR_DELAY": "mean","DEP_DELAY":"mean"}).reset_index().set_index('AIRLINE_NAME').sort_values('ARR_DELAY')
    res1=res.plot.bar()
    fig=res1.get_figure()
    fig.subplots_adjust(bottom=0.5)
    ax_list = fig.axes
    plt.title('Airlines avarage Delays')
    plt.show()
    fig.savefig('SRC/plotAirline.jpg')
    res.to_csv("SRC/airlines.csv")
    
    return res

def plotBestAirport(df1):
    res=df1.groupby("AIRPORT_NAME").agg({"ARR_DELAY": "mean","DEP_DELAY":"mean"}).reset_index().set_index('AIRPORT_NAME').sort_values('ARR_DELAY')[0:5]
    res1=res.plot.bar()
    fig=res1.get_figure()
    fig.subplots_adjust(bottom=0.5)
    plt.title('BestAirport avarage Delays')
    plt.show()
    fig.savefig('SRC/airport.jpg')
    res.to_csv("SRC/airport.csv")
    
    return res

def plotWorstAirport(df1):
    res=df1.groupby("AIRPORT_NAME").agg({"ARR_DELAY": "mean","DEP_DELAY":"mean"}).reset_index().set_index('AIRPORT_NAME').sort_values('ARR_DELAY',ascending=False)[0:5]
    res1=res.plot.bar()
    fig=res1.get_figure()
    fig.subplots_adjust(bottom=0.5)
    plt.title('WorstAirport avarage Delays')
    plt.show()
    fig.savefig('SRC/airport.jpg')
    res.to_csv("SRC/airport.csv")
    return res
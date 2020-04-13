import pandas as pd
import numpy as np
import json
from functions import plotTime, plotAirline, plotBestAirport, plotWorstAirport, sendMail
from generatePDF1 import generatePDF1
import smtplib
import base64


def CreateReport(airlineCode=None,time=0,depAirport=None,arrAirport=None,depDelay=True, best=False):
    #Creates a report filtering the database according to the parameters given
    data1 = pd.read_csv (r"SRC/delays_clean_small.csv", encoding='latin-1')
    df1 = pd.DataFrame(data1)
    df_analysis=df1
    
    #import the dictionary to fetch the airport name given the iata code
    f = open('d.json',)   
    # returns JSON object as a dictionary 
    data = json.load(f) 
    f.close() 
   
    outputString=''
    
    if depDelay==False:
        df_analysis['DELAY']=df1['ARR_DELAY']
        #if country:
            #df_analysis=df_analysis[df_analysis['ARR_STATE'] == country ]
        outputString += 'You are visualizing the arrival delays data.\n\n'
        
    else:
        df_analysis['DELAY']=df1['DEP_DELAY']
        outputString += 'You are visualizing the arrival delays data.\n\n'
        #if country:
            #df_analysis=df_analysis[df_analysis['DEP_STATE'] == country ]
            #outputString += f'Airport location = {country}\n'
                  
    
    if depAirport:
        df_analysis=df_analysis[df_analysis['ORIGIN'] == depAirport ]
        Airport=data[depAirport]
        outputString += f'Departure Airport = {Airport}\n'
        
    if arrAirport:
        df_analysis=df_analysis[df_analysis['DEST'] == arrAirport ]
        location=df_analysis.iloc[1,27]
        outputString += f'Arrival Airport = {location}\n'
    
    if airlineCode:
        try:
            df_analysis=df_analysis[df_analysis['OP_CARRIER'] == airlineCode]  
            airlineName=df_analysis.iloc[1,24]
            outputString += f'Airline = {airlineName}\n'
        except:
            return 'The airline is not operating between these airports'
     
    if time==1:
        df_analysis=df_analysis[df_analysis['MONTH'] == 1 ]
        outputString += f'Time Span = December 2018\n'
    else:
        outputString += f'Time Span = year 2018\n' 

    #-------------------------------------------------------------------------
    #basic statistics    
    mean=df_analysis['DELAY'].mean()
    outputString += f'mean delay = {mean}\n'    
    
    
    maxd=df_analysis['DELAY'].max()#show the maximum delay
    outputString += f'max delay = {maxd}\n'
        
       
    mind=df_analysis['DELAY'].min()#show the minimum delay
    outputString += f'min dealy = {mind}\n'
    
    stdd=df_analysis['DELAY'].std()
    outputString += f'std delay = {stdd}\n'
    
    #if the dataframe is empty it means the input parameters were not a valid input
    if df_analysis.shape[0]==0:
        outputString='There is no flight connection between these airports'
    
    print(outputString + '\n')
    
    
    #------------------------------------------------------------------------------
    #plotTime
    df_analysis["2MONTHS_BINS"] = pd.cut(df_analysis.MONTH, bins=[0,2,4,6,8,10,12],
                         labels=['01-02','03-04','05-06','07-08','09-10','11-12'])
    res=plotTime(df_analysis)  
    print(res)
    print('\n')

    #plotAirline
    res=plotAirline(df_analysis)
    print(res)
    print('\n')

    #plotBestAirport
    if best:
        res=plotBestAirport(df_analysis)
        print(res)
        print('\n')
    else:
        res=plotWorstAirport(df_analysis)
        print(res)
        print('\n')
    ##################################################################################
    #PDF GENERATION
    
    generatePDF1()
    
    ##################################################################################
    #email 

    filename = "OUTPUT/report.pdf"
    address='tzvuccyseraf@gmail.com'

    sendMail(address,filename,outputString)
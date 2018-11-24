# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 17:54:23 2018

@author: SARTHAK RAWAT
"""#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=NSE:IOC&interval=1min&apikey=QYOWP5SXIHB6BV3X

from tkinter import *
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import time
from os import system


def insert():
    ticker1 = name1_field.get()
    ticker2 = name2_field.get()
    ticker3 = name3_field.get()
    ticker4 = name4_field.get()
    
    #root.destroy()
    '''
    ticker1 = 'MSFT'
    ticker2 = 'MSFT'
    ticker3 = 'MSFT'
    ticker4 = 'MSFT'
      '''  
    while(1):      
        
        ts1 = TimeSeries(key='QYOWP5SXIHB6BV3X', output_format='pandas')
        data, meta_data = ts1.get_intraday(symbol= ticker1, interval='1min', outputsize='compact')
        #x1 = data['4. close']
        x1 = data.iloc[1:10, 3]
        
        ts2 = TimeSeries(key='QYOWP5SXIHB6BV3X', output_format='pandas')
        data, meta_data = ts2.get_intraday(symbol= ticker2, interval='1min', outputsize='compact')
        #x2 = data['4. close']
        x2 = data.iloc[1:10, 3]
        
        ts3 = TimeSeries(key='QYOWP5SXIHB6BV3X', output_format='pandas')
        data, meta_data = ts3.get_intraday(symbol= ticker3, interval='1min', outputsize='compact')
        #x3 = data['4. close']
        x3 = data.iloc[1:10, 3]
        
        ts4 = TimeSeries(key='QYOWP5SXIHB6BV3X', output_format='pandas')
        data, meta_data = ts4.get_intraday(symbol= ticker4, interval='1min', outputsize='compact')
        #x4 = data['4. close']
        x4 = data.iloc[1:10, 3]
                
        #system('%clear')
        #plt.autoscale(enable=False, axis='x', tight=None)
        plt.subplot(3,3,1)
        plt.plot(x1.tail(10),color="blue")
        plt.title(ticker1)
        plt.xlabel("Time")
        plt.ylabel("Price")
        
        plt.subplot(3,3,3)
        plt.plot(x2.tail(10),color="red")
        plt.title(ticker2)
        plt.xlabel("Time")
        plt.ylabel("Price")
        
        plt.subplot(3,3,7)
        plt.plot(x3.tail(10),color="green")
        plt.title(ticker3)
        plt.xlabel("Time")
        plt.ylabel("Price")
        
        plt.subplot(3,3,9)
        plt.plot(x4.tail(10),color="yellow")
        plt.title(ticker4)
        plt.xlabel("Time")
        plt.ylabel("Price")
        
        
        plt.show()
        time.sleep(30)
        #sleep(10)
        #plt.close(figure1)
        
        #print('hello 1')
        
        #plt.pause(10)
        
        
         
        #print('hello 2')
        

        #plt.close('all')

    
root = Tk()

root.configure()
root.title("TIKER")

root.geometry("200x200")

name1 = Label(root,text = "Ticker1")
name2 = Label(root,text = "Ticker2")
name3 = Label(root,text ="Ticker3")
name4 = Label(root,text ="Ticker4")

name1_field = Entry(root)
name2_field = Entry(root)
name3_field = Entry(root)
name4_field = Entry(root)

name1.grid(row = 0,column = 0)
name2.grid(row = 1,column = 0)
name3.grid(row = 2,column = 0)
name4.grid(row = 3,column = 0)

name1_field.grid(row = 0,column=1)
name2_field.grid(row = 1,column=1)
name3_field.grid(row = 2,column=1)
name4_field.grid(row = 3,column=1)

submit = Button(root,text = "Submit",bg = "Red",command = insert)
submit.grid(row = 4,column = 1)

root.mainloop()
"""
ticker1 = 'MSFT'

ts = TimeSeries(key='QYOWP5SXIHB6BV3X', output_format='pandas')
data, meta_data = ts.get_intraday(symbol= ticker1, interval='1min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()
"""
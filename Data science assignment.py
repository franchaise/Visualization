# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 19:29:17 2022

@author: Lenovo
"""

""" A graphical representation of the top 5 health-related causes of death 
    in the United Kingdom between the years 1990 to 2019"""
    
    
 #Importing python libraries to read csv files and perform graphs and plots by using python script   
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Loading CSV file into Pandas DataFrame to read CSV file
my_data = pd.read_csv('cause_of_deaths.csv')
df_my_data = pd.DataFrame(my_data)

#Filtering data to United Kingdom health-related deaths only
UK_diseases = df_my_data[df_my_data["Country/Territory"]
              =='United Kingdom'].set_index('Year')


#Determining the most frequent diseases across the years
#Subsetting the dataframe for diseases columns
UK_diseases = UK_diseases.iloc[ : , 2 : ]

#Summing values in columns of a dataframe
def sum_columns(df, a):
    '''function sums values in a column'''
    x = df.sum(axis = a)
    return x

UK_diseases_sum = sum_columns(UK_diseases, 0)

#Sorting summed values
def sort(val, type):
    return val.sort_values(ascending = type)
    '''sorts values '''
UK_diseases_sum_sorted = sort(UK_diseases_sum, False)

summary_table_top_5 = pd.DataFrame(UK_diseases_sum_sorted.head(5),
                                   columns = ['sum'])

#Analyzing for top 5 diseases
top_5_diseases = ('Cardiovascular Diseases', 'Neoplasms',
                  'Chronic Respiratory Diseases',
                  'Lower Respiratory Infections', 'Digestive Diseases')

UK_top_5 = UK_diseases.loc[ : , top_5_diseases]

#Plotting Line Graph
#Setting parameters for Line Graph
def line_plot(data, title, x_label, y_label, legend_data):
    '''plots a line chart'''
    plt.figure(figsize = (10,5))
    data.plot(legend = True)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(legend_data, fontsize = 7)
    return plt.show()
    
title1 = 'UK top 5 diseases'
x_label1 = 'Year'
y_label1 = 'Count'
legend_data1 = top_5_diseases

line_plot(UK_top_5, title1, x_label1, y_label1, legend_data1)

#Plotting Bar Chart
#Setting parameters for Bar Chart
def bar_plot(x_category, y_values, title, x_label, y_label):
    '''plots a bar chart'''
    plt.figure(figsize = (10,6))
    plt.barh(x_category, y_values, color = ['teal', 'cyan', 'Tomato',
                                            'green', 'black'])
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    return plt.show()

title2 = 'UK TOP 5 DISEASES'
x_label2 = 'TOTAL COUNT (Millions)'
y_label2 = 'DISEASE TYPE'

bar_plot(summary_table_top_5.index, summary_table_top_5['sum'],
         title2, x_label2, y_label2)


#Plotting pie chart
#Setting parameters for pie chart
def pie_chart(data, title, pie_label):
    ''' plots pie chart'''
    plt.figure(figsize =(10, 7))
    for i in range(len(data)):
        plt.pie(data[i], labels =pie_label)
        plt.title(title)
        return plt.show()

data3 =[summary_table_top_5['sum']]
pie_label = top_5_diseases
pie_chart(data3, title1, pie_label )
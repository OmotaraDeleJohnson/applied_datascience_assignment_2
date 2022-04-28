#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 17:39:26 2022

@author: omotaradele-johnson
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





#Instruction 1
# A function that takes indicators filenames as argument&reads Dataframes into 2(as columns and year)
# Indicator1 - Dataframe1( to make the years the columns)    
def createDf(file_path):
    columnby_year = pd.read_excel(file_path)
    clm_year = columnby_year.head(5)
    print("Get column by year\n\n",clm_year)
    
    
    # Indicator1 - Dataframe2(to make country names the column)
    columnby_country = columnby_year.set_index("Country Name").transpose()
    print("Get column by country \n\n",columnby_country.head())
    
    
    return columnby_country


def createDf2(file_path1,file_path2):
    dfE = pd.read_excel(file_path1).set_index("Country Name").transpose()
    
    dfU = pd.read_excel(file_path2).set_index("Country Name").transpose()
    
    return dfE,dfU

def africanCorrelation(file_path1,file_path2):
    dfE,dfU = createDf2(file_path1, file_path2)
    
    Africa_Access2_eltrcity = dfE.iloc[:, 5:8]
    print(Africa_Access2_eltrcity)
    Africa_urban_pop = dfU.iloc[:, 4:7]
    print(Africa_urban_pop)
    #Nigeria access to electricity vs Nigeria urban population
    N_Accs2_Elct= Africa_Access2_eltrcity["Nigeria"]
    N_urb_pop = Africa_urban_pop["Nigeria"]
    cor_Ng = N_Accs2_Elct. corr(N_urb_pop)
    cor_Ng
    
    #Ghana access to electricity vs Ghana urban population
    G_Accs2_Elct= Africa_Access2_eltrcity["Ghana"]
    G_urb_pop = Africa_urban_pop["Ghana"]
    cor_Gh = G_Accs2_Elct. corr(G_urb_pop)
    cor_Gh
    
    #South Africa access to electricity vs South Africa urban population
    SA_Accs2_Elct= Africa_Access2_eltrcity["South Africa"]
    SA_urb_pop = Africa_urban_pop["South Africa"]
    cor_SA = SA_Accs2_Elct. corr(SA_urb_pop)
    
    return cor_Ng,cor_Gh,cor_SA

def europeanCorrelation(file_path1,file_path2):
    dfE,dfU = createDf2(file_path1, file_path2)
    #European countries
    European_Accs2_elt = dfE.iloc[:, 2:5]
    European_Accs2_elt
    
    Europe_urban_pop = dfU.iloc[:, 7:10]
    Europe_urban_pop
    
    #Italy access to electricity vs Italy urban population
    cor_It = European_Accs2_elt["Italy"]. corr(Europe_urban_pop['Italy'])
    cor_It
   
    #Ukraine access to electricity vs Ukraine urban population
    cor_Ukr = European_Accs2_elt["Ukraine"]. corr(Europe_urban_pop['Ukraine'])
    cor_Ukr
    #UK access to electricity vs UK urban population
    cor_UK = European_Accs2_elt["United Kingdom"]. corr(Europe_urban_pop['United Kingdom'])
    cor_UK
    
    return cor_It,cor_Ukr,cor_UK



def compareEuroDataWithWorld(file_path):
    df = createDf(file_path)
    df.describe()
    
    #Instruction 2
    # To cross-compare summary statistics between individual countries and the whole world
    
    world = df.iloc[:, -1]
    world
   
    #Summary statistics of world data
    world.describe()
    
    #cross comparing with 3 countries grouped in Europe
    European_Accs2_elt = df.iloc[:, 2:5]
    European_Accs2_elt
    
    #Summary statistics of world data
    European_Accs2_elt.describe()
    
    #to place the value side by side for comparison
    compare_sidebyside = [world, European_Accs2_elt]
    return compare_sidebyside

def compareEuroDataWithGrapgh(file_path):
    df2 = createDf(file_path)
    European_Accs2_elt = df2.iloc[:, 2:5]
    #plot the european countries values to show their access to electricity value
    Years = European_Accs2_elt.index.astype(float)
    print(Years)
    ECountries = European_Accs2_elt.iloc[:, 0:3]
    print(ECountries)
    
    plotGraph(Years, ECountries, 'European percentage access to electricity', 'Years', 'European countries access to electricity', ['Italy', 'Ukraine', 'United Kingdom'])
    
def plotGraph(x_value,y_value,y_label,x_label,plot_title,labelArr):
        plt.plot(x_value, y_value, label=labelArr)
        plt.ylabel(y_label)
        plt.xlabel(x_label)
        plt.title(plot_title)
        plt.xticks(x_value)
        plt.yticks([20, 40, 60, 80, 100])
        plt.legend()
        plt.show
        
def compareAfricaDataWithGrapgh(file_path):
    df3 = createDf(file_path)
    # group 3 african countries to determine its summary statistics in comparison with the world
    Africa_Access2_eltrcity = df3.iloc[:, 5:8]
    print(Africa_Access2_eltrcity)
    
    #Summary statistics of african data
    Africa_Access2_eltrcity.describe()
    
    Year = Africa_Access2_eltrcity.index.astype(float)
    print(Year)
    Countries = Africa_Access2_eltrcity.iloc[:, 0:3]
    print(Countries)
    
    plotGraph(Year, Countries, 'African percentage access to electricity', 'Year', 'African countries access to electricity', ['Nigeria', 'Ghana', 'South Africa'])
    
 
#Getting DataFrame for urban Population
createDf("./Urban_population_extract.xlsx")
 
#Getting DataFrame for Access To Electricity   
createDf("./Access_to_Electricity_Extract.xlsx")

#Returns dataframe for both access to electricity and urban population indicators
createDf2("./Access_to_Electricity_Extract.xlsx","./Urban_population_extract.xlsx")


#Comparing side by side access to electicity between europe and world
compareEuroDataWithWorld("./Access_to_Electricity_Extract.xlsx")

#showing the trend of access to elctricity for european countries(Italy,Ukraine,United Kingdom)
compareEuroDataWithGrapgh("./Access_to_Electricity_Extract.xlsx")

#showing the trend of access to elctricity for african countries(Nigeria,Ghana,South Africa)
compareAfricaDataWithGrapgh("./Access_to_Electricity_Extract.xlsx")

#correlation between access to electricity and urban population for european countries(Italy,Ukraine,United Kingdom)
europeanCorrelation("./Access_to_Electricity_Extract.xlsx", "./Urban_population_extract.xlsx") 

#correlation between access to electricity and urban population for african countries(Nigeria,Ghana,South Africa)
africanCorrelation("./Access_to_Electricity_Extract.xlsx", "./Urban_population_extract.xlsx")

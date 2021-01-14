#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thursday Dec  17  2020 17 22:06

@author: benedictusvanhoof
"""

import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import sqlite3


def load_data(events_filepath):
    '''
    input : a csv file
    output : a pandas dataframe based on the csv file
    '''
    df_hf = pd.read_csv(events_filepath)
    
    return df_hf




def clean_data(df):
    
    '''
    Input : A non-cleaned dataframe
    Output: The  same dataframe but cleaned
    '''
    
    ## change od the dtype of the age and the platelets columns
    df['age']= df['age'].astype(int)
    df['platelets']= df['platelets'].astype(int)
    number_columns = df.shape[1]
    ## Drop the column 'time' and the binary columns. They will no be part of the model
    print ("number of columns in dataframe before deleting the columns : ", number_columns)
    df.drop(columns=['age','time','anaemia','diabetes','smoking','sex',
                    'high_blood_pressure'],inplace=True)
    number_columns = df.shape[1]
    print ("nr columns in dataframe after deleting the columns not incl analysis : ", number_columns)  
    ## Rename the columns DEATH_EVENT,creatine_phosphokinase, high_blood_pressure and sex
    df.rename(columns={'DEATH_EVENT':'death_event','creatinine_phosphokinase':'creat_phosphok',},inplace=True)
    ## calculate the outliers and store them into a dictionary
    ## initialize a list with the column names to be checked for outliers
    list_columns = ['creat_phosphok','ejection_fraction','platelets',
                'serum_creatinine','serum_sodium']

    ## Dealing with the outliers
    outliers = {}
    print("{0:15}{1:10}{2:15}{3:10}{4:10}{5:15}".format("","feature","","Lower Border","","Upper Border"))
    for column in list_columns:
        list_borders = []
         ## calculate the outliers for ejection_fraction
        q3, q1 = np.percentile(df[column], [75,25])
        ## inter-quartile range
        iqr = q3 - q1
        ##calculate the ouliers limits
        ## (1,5 times the iqr)
        upper = q3 + 1.5*iqr
        list_borders.append(upper)
        lower = q1 - 1.5*iqr
        list_borders.append(lower)
        outliers[column] = list_borders
        print("{0:15}{1:25}{2:10.2f}{3:10}{4:10.2f}".format("Outliers",column,lower,"",upper))

    ## call the function kill_outliers to delete the outliers lines
    print ("The dataframe has ",df.shape[0]," lines before the suppression of the outliers")
    for key,value in outliers.items():

        column = key
        upper = value[0]
        lower = value[1]    
        df = kill_outliers (df,column,upper,lower)
    print ("The dataframe has ",df.shape[0]," lines after the suppression of the outliers")
        


    return df
## function to get rid of the outliers
def kill_outliers (df,var,uppercriteria,lowercriteria):
    '''
    Input  : a dataframe
           : a columns
           : a lower and upper border
    output : a dataframe with the outliers deleted    
    '''
    df = df[(df[var] > lowercriteria) & (df[var] < uppercriteria)]
    return df
                

def save_data(df_hf, database_filepath):
    '''
    input : a cleaned dataframe and  a path for and sqllite database
    The function doesn't return anything
    '''
    database_filepath = 'sqlite:///' + database_filepath
    engine = create_engine(database_filepath)
    df_hf.to_sql('HeartFailuresEvents', engine,if_exists='replace' ,index=False)
    
    

def main():   
     
    if len(sys.argv) == 3:

        events_filepath, database_filepath = sys.argv[1:]
        print('{0:20}{1:25}'.format('Loading data...\n',events_filepath))
              

              
        my_df = load_data(events_filepath)

        print('Cleaning data...')
        
        my_df = clean_data(my_df)

        
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        
        
        
        save_data(my_df, database_filepath)
        
        print('Cleaned data saved to database!')
       

    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'heart_failure_clinical_records_dataset.csv '\
              'HartFailure.db')


if __name__ == '__main__':
    main()   
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 30 2020

@author: benedictus vanhoof
"""

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import fbeta_score, accuracy_score, precision_score,recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle
from imblearn.over_sampling import SMOTE






import sys







def load_data(database_filepath):
    '''
    This function loads the data from an sqllite database into a    
    dataframe df
    input : the path to the sqllite database
    output : a pandas dataframe
    '''
    
    database_filepath = 'sqlite:///' + database_filepath
    engine = create_engine(database_filepath)            
    df = pd.read_sql("SELECT * FROM HeartFailuresEvents", engine)
    X = df.iloc[:,0:5].values
    y = df.iloc[:,5].values
    print ("There are " ,X.shape[0], "lines in the dataset")
    
    return X, y 

## Oversample the minority with SMOTE (synthetic minority oversampling technique)
def my_oversample(X,y):
    '''
    This function oversamples the minority
    Input: an array with the features 
         : an array with the labels y
    Output : Two arrays where the labales are balanced


    '''
    oversample = SMOTE(random_state = 1)
    X_oversample, y_oversample = oversample.fit_resample(X,y)      
    return X_oversample,y_oversample

             

def build_model( X,y):

    '''
    input : The features and the labels from de database
    output:the model, the labels, and the predicted data
    This function builds the classifier model (Random Forest) with Pipeline and GridSearch)
    As input it takes the numpay arrays with the features and the labels
    '''        
    ## Create the training and test data set
    

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=1)

          
    learner = RandomForestClassifier(class_weight='balanced', n_estimators=120,
                       random_state=1)
    
    learner.fit(X_train, y_train)
    predictions_test = learner.predict(X_test)
    print("Results for :",learner)
    print("Evaluation Scores         Test ")
    
    print("{0:25}{1:.2f}".format("Accuracy :",accuracy_score(y_test, predictions_test)))
    print("{0:25}{1:.2f}".format("F_beta :",fbeta_score(y_test,predictions_test,beta=1)))
    print("{0:25}{1:.2f}".format("Recall",recall_score(y_test,predictions_test)))
    print("{0:25}{1:.2f}".format("precision",precision_score(y_test,predictions_test)))
    print("\n")
    
    
    
    
     
    
    

    
    return learner,y_test,predictions_test




                    
   




def evaluate_model(y,predicted):
    '''
    This function calculates the accuracy, precision, recall and prints out the classification report
    The input is the true test labels and the predicted labels
    The function doesn't return anything
    
    
    '''
    
    ## Calculate the accuracy score as a proportion
    #ac_sc = accuracy_score(y, predicted,normalize=True, sample_weight=None)
    ac_sc = accuracy_score(y, predicted)
    print ("Accuracy score :", ac_sc) 
    ## Calculate the precision score
    #pr_sc = precision_score(y, predicted,labels=None, average='micro', sample_weight=None, zero_division='warn')
    pr_sc = precision_score(y, predicted)  
    print ("Precision score :", pr_sc)
    ## Calculate the recall score
    #re_sc = recall_score(y, predicted,labels=None, average='micro', sample_weight=None, zero_division='warn')
    re_sc = recall_score(y, predicted)
    print ("Recall score :", re_sc) 
    ## Calculate the recall score
    #re_sc = recall_score(y, predicted,labels=None, average='micro', sample_weight=None, zero_division='warn')
    fb_sc = fbeta_score(y, predicted,beta=1)
    print ("F_beta score :", fb_sc) 
    ## print out the classification report
    ##target_names = category_names
    #print(classification_report(y_test,predicted, target_names=target_names, zero_division=0))
   


    
    


def save_model(model, model_filepath):
    with open(model_filepath, 'wb') as file:
        
        pickle.dump(model, file)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        ## loding the data
        X, y = load_data(database_filepath)
        print ("Nr of lines before oversampling :" , X.shape[0] )
        ## oversampling
        X, y = my_oversample(X,y)
        print ("Nr of lines after oversampling :" , X.shape[0] )
       
        ## building the model
        print('Building model...')
        model, y, predicted = build_model(X,y)       
        
        print('Evaluating model...')  
        evaluate_model( y, predicted)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
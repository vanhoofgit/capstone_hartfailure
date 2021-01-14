
from flask import Flask
from flask_wtf.form import _is_submitted
app = Flask(__name__)
app.config['SECRET_KEY']='f049f7b1ad3132ccb604e345e00cbe60'
from flask import render_template,request
import sys
sys.path.append('hartfailure')
import forms
import json
import plotly
import joblib
from plotly.graph_objects import Bar, Scatter,heatmap
import plotly.figure_factory as ff 
import numpy as np
import pandas as pd
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, BooleanField,FloatField, PasswordField, SubmitField
from sklearn.ensemble import RandomForestClassifier
from sqlalchemy import create_engine
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
Bootstrap(app)

# load data
engine = create_engine('sqlite:///data/heartfailure.db')
df = pd.read_sql_table('HeartFailuresEvents', engine)

# load model
model = joblib.load("models/classifier.pkl")
X,y = df.iloc[:,:5].values,df.iloc[:,5].values
#model = RandomForestClassifier()
model.fit(X,y)

## calculation of the feature importances
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]
columns = df.columns.values[indices[:5]]
values = importances[indices][:5]
print(columns)



# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():

    ## preparation of the graph
    count = 500
    xScale = np.linspace(0, 100, count)
    y0_scale = np.random.randn(count)
    y1_scale = np.random.randn(count)
    y2_scale = np.random.randn(count)

    # Create traces
    trace0 = plotly.graph_objects.Scatter(
        x = xScale,
        y = y0_scale
    )
    trace1 = plotly.graph_objects.Scatter(
        x = xScale,
        y = y1_scale
    )
    trace2 = plotly.graph_objects.Scatter(
        x = xScale,
        y = y2_scale
    )




    
    
    
    
    ## Transformation of the trace to a json format

    data = [trace1,trace2,trace2]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder) 

    my_tekst = 'hier staat iets' 
    
    return render_template('master.html',graphJSON=graphJSON,my_tekst=my_tekst)

    


# web page that handles user query and displays model results
@app.route('/graphs')
def graphs():
    print(df.head())
    list_titles= df.columns
    list_subtitles = ['Microgram/L','% Pumped Out',
                  'Kiloplatets/Ml','Miligram/Dl','MilliEquivalent/L','No/Yes']
    
    
    
    # Create traces
    # preparation for the heatmap
    df_temp = df.copy()
    df_temp = df_temp.corr()
    z = df_temp.values

    

    
    
    
     
   

    graphs= [{
    "data": [
        {
            "x": df.columns
            ,
            "y": df.columns
            ,
            "z":df_temp.values,
            "type": "heatmap",
            
        }
    ],
    "layout":{
                
                'title': 'Correlation between the features and label',
                
                'yaxis': {
                    'title': "Features and label",
                    'titlefont' :{'size':10},
                    'tickfont'  :{'size':8}
                    
                },
                'xaxis': {
                    'title': "Features and label",
                    'titlefont' :{'size':13},
                    'tickfont'  :{'size':8}
                }
             }
        
    },
    {'data': [
                Bar(
                    x = np.arange(5),
                    y = values,
                    name='Feature'
                ),
                Bar(
                    x= np.arange(5),
                    y=np.cumsum(values),
                    name='Cummulative Features'
                )
                
            ],
        'layout':{
                
                'title': 'Feature Importance',
                'yaxis':{'title':'% of explanation',
                         'titlefont':{'size':10},
                         'tickfont': {'size':8}
                },
                'xaxis':{'title':'Feature',
                         'titlefont':{'size':13},
                         'tickfont': {'size':8},
                         'tickvals': np.arange(5),
                         'ticktext': columns
                }

                }


    }   
     ]            
    #graphJSON = json.dumps(graphs,cls=plotly.utils.PlotlyJSONEncoder)
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # This will render the graphs.html Please see that file. 
    return render_template(
        'graphs.html',graphJSON=graphJSON,ids=ids
        
    )
    

@app.route('/predict',methods=['GET','POST'])
def predict():   
    form = forms.PredictForm()

    if form.validate_on_submit():
        comment = 'Validation of Data Succeeeded'
        result = request.form
        #list_features =['creatinine_phosphokinase (mcg/l)','ejection_fraction (%)','platelets (kiloplat/ml)','serum_creatinine (mg/dl)','serum_sodium (mEq/l)']
        list_features =['creat_phosphok','ejection_fraction','platelets','serum_creatinine','serum_sodium']
        
        
        ## initialization of the list, used for the prediction
        list_prediction_values =[]
        ## initialization of a dictionary for the printout of the predictions
        my_results = {}
        
        for feature in list_features:
            ## the  necessary values from the result dictionary are attached to the prediction list
            list_prediction_values.append(result[feature])
            ## the  necessary values from the result dictionary are attached to the dictionary used for the printout
            my_results[feature] = result[feature]
            
        ## make the prediction based on the input vales
        prediction_values = np.array(list_prediction_values).reshape(1,-1)
       
        my_prediction= model.predict(prediction_values)
        if my_prediction == 1:

            personal_message = "You are in danger!"
        else:
            personal_message = "You are safe !"


            
        return render_template('my_input.html',result=result,comment= comment,list_prediction=list_prediction_values,my_results=my_results,personal_message=personal_message)
        
    return render_template('predict.html',title = 'Test your Heart Failure Risk :',title2='Fill in the form and click Validate', form=form) 



def main():
    
    #application.run(host='0.0.0.0', port=5000, debug=True)
    app.run()


if __name__ == '__main__':
    main()





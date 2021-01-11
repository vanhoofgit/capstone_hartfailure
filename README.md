# capstone_heart_failure
A machine learning project to make a classifier for possible heart failure.


**1)Project Motivation**</br>
Heart desease is still one of the leading causes of death worldwide. The aim of the project was to build a binary machine learning classifier that would be able to predict an imminent heart failure

**2)Libraries**</br>
The following Python libraries should be installed:</br>
click==7.1.2
dnspython==2.1.0
dominate==2.6.0
email-validator==1.1.2
Flask==1.1.2
Flask-Bootstrap==3.3.7.1
Flask-WTF==0.14.3
gunicorn==20.0.4
idna==3.1
imbalanced-learn==0.7.0
imblearn==0.0
itsdangerous==1.1.0
Jinja2==2.11.2
joblib==1.0.0
MarkupSafe==1.1.1
numpy==1.19.4
pandas==1.1.4
plotly==4.13.0
python-dateutil==2.8.1
pytz==2020.4
retrying==1.3.3
scikit-learn==0.24.0
scipy==1.5.4
six==1.15.0
SQLAlchemy==1.3.20
threadpoolctl==2.1.0
visitor==0.1.3
Werkzeug==1.0.1
WTForms==2.3.3

The following installatuions were done :
 pip3 install pandas

**3) Files:**</br>
The source file is a csv file, downloaded from Kaggle :
</br>
It is a small file with 13 columns which describe a number of medical, physical and social parameters
</br>
**4)Run the Application:**
<br>
To run ETL pipeline that cleans data and stores in a database,from the root directory , type:</br>
python data/process_data.py data/heart_failure_clinical_records_dataset.csv data/heartfailure.db 
<br>
<br>
To run the ML pipeline, type:</br>
python models/train_predict.py data/heartfailure.db models/classifier.pkl
<br>
<br>
To start the web app and test the classifier, from the root directory of the project type:</br>
python app/run.py
<br>
<br>
Go to http://0.0.0.0:5000
</br>
</br>  

**5)Results** </br>
After running the scripts (see above 4)) a webpage is available.
On the webpage are shown a few charts about the messages genres and categories and you can type in a message. The classifier will attach the message to a message category.


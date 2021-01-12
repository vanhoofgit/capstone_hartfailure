# capstone_heart_failure
A machine learning project to make a classifier for possible heart failure.


**1)Project Motivation**</br>
Heart desease is still one of the leading causes of death worldwide. The aim of the project was to build a binary machine learning classifier that would be able to predict an imminent heart failure

**2)Libraries**</br>
The following installations were done in my virtual environment :</br>
pip3 install pandas</br>
pip3 install sqlalchemy</br>
pip3 install imblearn</br>
(This installs joblib,threadpoolctl,scipy,scikit-learn, imbalanced-learn, imblearn</br>
pip3 install flask</br>
(This install also itsdangerous, MarkupSafe, Jinja2, click, Werkzeug)</br>
pip3 install flask_wtf
(This installs also WTForms)</br>
pip3 install flask_bootstrap
pip3 install email_validator
pip3 install plotly


Content of the requirements.txt file:







**3) Files:**</br>
The source file is a csv file, downloaded from Kaggle :</br>
https://www.kaggle.com/andrewmvd/heart-failure-clinical-data
</br>
It is a small file with 13 columns which describe a number of medical, physical and social parameters
</br>
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
Goto localhost://0.0.0.0:5000
</br>
</br>  

**5)Results** </br>
After running the scripts (see above 4)) a webpage is available.
On the webpage are shown a few charts about the messages genres and categories and you can type in a message. The classifier will attach the message to a message category.


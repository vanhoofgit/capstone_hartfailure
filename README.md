# capstone_heart_failure
A machine learning project to make a classifier for possible heart failure.


**1)Project Motivation**</br>
The aim of the project was to build a classifier that would be able to predict a imminent heart failure

**2)Libraries**</br>
The following Python libraries should be installed:</br>

**3) Files:**</br>
The files are download from Figure Eight : https://appen.com. There are two files. 'disaster_categories.csv' contains a message id and 36 message categories columns that indicate with a zero or one whether that message belongs to that message category or not. 'desaster_message.csv'contains the same message id, the message text in English, the message text in the original language and a message genre.
</br>
</br>
**4)Run the Application:**
</br>
To run ETL pipeline that cleans data and stores in a database,from the root directory , type: </br>
python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db 
</br>
To run the ML pipeline, type:</br>
python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
</br>
To start the web app and test the classifier, from the root directory of the project type:</br>
python app/run.py</br>
Go to http://0.0.0.0:3001
</br>
</br>  

**5)Results** </br>
After running the scripts (see above 4)) a webpage is available.
On the webpage are shown a few charts about the messages genres and categories and you can type in a message. The classifier will attach the message to a message category.


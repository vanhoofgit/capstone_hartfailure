from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField,IntegerField, BooleanField,FloatField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange, Regexp
class PredictForm(FlaskForm):
    
    creat_phosphok = IntegerField('Creatinine Phosphokinase', validators=[NumberRange(min=20,max=7800,message='value between 20 and 7800')])  
    ejection_fraction = IntegerField('Ejection Fraction', validators=[NumberRange(min=15,max=80,message='value between 15 and 80')])  
    platelets = IntegerField('Platelets', validators=[NumberRange(min=25000,max=850000,message='value between 25000 and 850000')])
    serum_creatinine=FloatField('Serum Creatinine', validators=[NumberRange(min=0.50,max=9.50,message='value between 0.5 and 9.5')])
    serum_sodium = IntegerField('Serum Sodium', validators=[NumberRange(min=100,max=148,message='value between 100 and 148')])    
    submit = SubmitField('Make the Prediction')

class MyInputForm(FlaskForm):

    myName = StringField('Name',validators=[Regexp('a-zA-Z',message='Only A-Z a-z')])
    myEmail = StringField('E-mail',validators=[Email()])
    myage = IntegerField('Age',validators=[NumberRange(min=1,max=120,message='between 0 and 120')])
    submit = SubmitField('Make the Prediction')



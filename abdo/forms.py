from flask_wtf import FlaskForm
from wtforms import StringField , IntegerField ,PasswordField,BooleanField,SubmitField,TextField
from wtforms.validators import InputRequired , Length , any_of,DataRequired,EqualTo

class Register(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('New Password', validators=[DataRequired(),EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit   = SubmitField('Submit')
class Login(FlaskForm):
    email = StringField('email',default='',validators=[InputRequired(), Length(min=2, max=30)])
    password = PasswordField('password',default='', validators=[InputRequired(), Length( max=80)])
    remember = BooleanField('remember me')
    submit   = SubmitField('Submit')
class Post(FlaskForm):
    content = TextField('Post',default='',validators=[InputRequired(), Length(max=150)])
    submit   = SubmitField('Save')
class Message(FlaskForm):
    content = TextField('Message',default='',validators=[InputRequired(), Length(max=150)])
    submit   = SubmitField('Save')


#     def validate_on_submit(self):
#         """

#         :rtype: bool
#         """
#         if not Form.validate_on_submit(self):
#             return False

#         email = User.query.filter_by(
#             email=self.email.data.lower()).first()
#         username = User.query.filter_by(
#             username=self.username.data.lower()).first()
#         if username:
#             self.username.errors.append("That username is already taken")
#             return False
#         if email:
#             self.email.errors.append("That email is already taken")
#             return False
#         return True



# __all__form = (
#     'BooleanField', 'DecimalField', 'DateField', 'DateTimeField', 'FieldList',
#     'FloatField', 'FormField', 'IntegerField', 'RadioField', 'SelectField',
#     'SelectMultipleField', 'StringField', 'TimeField',
# )

# __all__form = (
#     'DataRequired', 'data_required', 'Email', 'email', 'EqualTo', 'equal_to',
#     'IPAddress', 'ip_address', 'InputRequired', 'input_required', 'Length',
#     'length', 'NumberRange', 'number_range', 'Optional', 'optional',
#     'Required', 'required', 'Regexp', 'regexp', 'URL', 'url', 'AnyOf',
#     'any_of', 'NoneOf', 'none_of', 'MacAddress', 'mac_address', 'UUID',
#     'ValidationError', 'StopValidation'
# )

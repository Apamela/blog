from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,PasswordField,RadioField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class BlogForm(FlaskForm):
    title = TextAreaField('Title',validators = [Required()])
    description = TextAreaField(" the blog you need",validators=[Required()])
    category = RadioField('Label', choices=[ ('gamesblog','gamesblog'), ('traditionalblog','traditionalblog'),('quotes','quotes'),('productblog','productblog')],validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[Required()])
	submit = SubmitField()

class UpdateBlogForm(FlaskForm):
    title = TextAreaField('Tell us about you.',validators = [Required()])
    image=TextAreaField('your images',validators=[Required()])
    description=TextAreaField(" the blog you need",validators=[Required()])
    submit = SubmitField('Submit')
class UpdateProfileForm(FlaskForm):
    bio = TextAreaField('Tell us about your you.',validators = [Required()])
    submit = SubmitField('Submit')

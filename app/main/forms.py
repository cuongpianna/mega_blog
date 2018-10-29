from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User
from app.auth.forms import RegistrationForm


class PostForm(FlaskForm):
    post = TextAreaField('Say some thing', validators=[DataRequired(), Length(min=6, max=200)])
    submit = SubmitField('Post')


class EditProfileForm(RegistrationForm, FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, origin_username, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.origin_username = origin_username

    def validate_username(self, username):
        if username.data != self.origin_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username')
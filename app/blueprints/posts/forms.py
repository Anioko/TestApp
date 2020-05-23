from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import RadioField, StringField, SubmitField, TextAreaField, MultipleFileField
from wtforms.validators import DataRequired, Length, Required

images = UploadSet('images', IMAGES)


class QuestionForm(FlaskForm):
    """ This is the question form  """
    title = StringField('Title', validators=[DataRequired(), Length(min=50, max=150)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=50, max=850)])
    submit = SubmitField('Submit')


class SubmitForm(FlaskForm):
    name = StringField('Name your community or area or interest!', [Required()])
    desc = TextAreaField('Description of interest!', [Required()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    # image = FileField('Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    text = TextAreaField('')
    photo = MultipleFileField('Add Photos', validators=[FileAllowed(images, 'Images only!')])
    post_privacy = RadioField('Privacy', choices=[('0', 'Everyone'), ('1', 'Followers Only'), ('2', 'Private')],
                              default='0')
    submit = SubmitField('Submit')

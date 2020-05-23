from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import Length, Required

images = UploadSet('images', IMAGES)


class PhotoForm(FlaskForm):
    photo = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    submit = SubmitField('Submit')


class ExtraForm(FlaskForm):
    photo = FileField('Upload CV only', validators=[FileRequired(), FileAllowed(images, 'Documents only!')])
    required_skill_one = SelectField(u'Do you meet this requirement?', choices=[('Yes', 'Yes'), ('No', 'No')])
    required_skill_two = SelectField(u'Do you meet this requirement?', choices=[('Yes', 'Yes'), ('No', 'No')])
    required_skill_three = SelectField(u'Do you meet this requirement?', choices=[('Yes', 'Yes'), ('No', 'No')])
    required_skill_four = SelectField(u'Do you meet this requirement?', choices=[('Yes', 'Yes'), ('No', 'No')])
    required_skill_five = SelectField(u'Do you meet this requirement?', choices=[('Yes', 'Yes'), ('No', 'No')])
    required_skill_six = SelectField(u'Do you meet this requirement?', choices=[('Yes', 'Yes'), ('No', 'No')])
    required_skill_seven = SelectField(u'Do you meet this requirement?', choices=[('Yes', 'Yes'), ('No', 'No')])
    required_skill_eight = SelectField(u'Do you meet this requirement?', choices=[('Yes', 'Yes'), ('No', 'No')])
    required_skill_nine = SelectField(u'Do you meet this requirement?', choices=[('Yes', 'Yes'), ('No', 'No')])
    required_skill_ten = SelectField(u'Do you meet this requirement?', choices=[('Yes', 'Yes'), ('No', 'No')])
    submit = SubmitField('Submit')


class QuestionForm(FlaskForm):
    """ This is the question form  """
    title = StringField('Title', validators=[Required(), Length(min=50, max=150)])
    description = StringField('Description', validators=[Required(), Length(min=50, max=250)])
    submit = SubmitField('Submit')


class AnswerForm(FlaskForm):
    """ This is the question answers form  """
    body = TextAreaField('Answers', validators=[Required(), Length(min=50, max=5000)])
    submit = SubmitField('Submit')


class MessageForm(FlaskForm):
    """ This is the messageform  """
    body = TextAreaField('Message', validators=[Required(), Length(min=50, max=5000)])
    submit = SubmitField('Submit')


class ReplyForm(FlaskForm):
    """ This is the message reply form  """
    body = TextAreaField('Reply', validators=[Required(), Length(min=50, max=5000)])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    """ This is the post(blog posts or articles) form  """
    body = TextAreaField('Post', validators=[Required(), Length(min=50, max=5000)])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    """ This is the comments form  """
    body = TextAreaField('Comments', validators=[Required(), Length(min=50, max=5000)])
    submit = SubmitField('Submit')


class InterestForm(FlaskForm):
    """ This is the interest declaration form  """
    interest_one = StringField('Professional networking')
    interest_two = StringField('Job Opportunities')
    interest_three = StringField('Career Questions, Advice & Support')
    interest_four = StringField('Communications between colleagues and co-workers')
    submit = SubmitField('Submit')

from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.fields import PasswordField, StringField, SubmitField, BooleanField, IntegerField, FloatField, \
    MultipleFileField, TextAreaField, SelectField, FileField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, EqualTo, InputRequired, Length

from app import db
from app.models import Role, User, MCurrency, MShippingMethod, MCategory

images = UploadSet('images', IMAGES)


class ChangeUserNameForm(FlaskForm):
    first_name = StringField(
        'First name', validators=[InputRequired()])
    last_name = StringField(
        'Last name', validators=[InputRequired()])
    submit = SubmitField('Update first name and last name')


class ChangeUserEmailForm(FlaskForm):
    email = EmailField(
        'New email', validators=[InputRequired(),
                                 Length(1, 64),
                                 Email()])
    submit = SubmitField('Update email')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')


class ChangeAccountTypeForm(FlaskForm):
    role = QuerySelectField(
        'New account type',
        validators=[InputRequired()],
        get_label='name',
        query_factory=lambda: db.session.query(Role).order_by('permissions'))
    submit = SubmitField('Update role')


class ConfirmAccountForm(FlaskForm):
    confirmed = BooleanField('True: Tick this checkbox to confirm the users account manually',
                             validators=[InputRequired()])
    submit = SubmitField('Confirm')


class InviteUserForm(FlaskForm):
    role = QuerySelectField(
        'Account type',
        validators=[InputRequired()],
        get_label='name',
        query_factory=lambda: db.session.query(Role).order_by('permissions'))
    first_name = StringField(
        'First name', validators=[InputRequired(),
                                  Length(1, 64)])
    last_name = StringField(
        'Last name', validators=[InputRequired(),
                                 Length(1, 64)])
    email = EmailField(
        'Email', validators=[InputRequired(),
                             Length(1, 64),
                             Email()])
    submit = SubmitField('Invite')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')


class NewUserForm(InviteUserForm):
    password = PasswordField(
        'Password',
        validators=[
            InputRequired(),
            EqualTo('password2', 'Passwords must match.')
        ])
    password2 = PasswordField('Confirm password', validators=[InputRequired()])

    submit = SubmitField('Create')


class MCategoryForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    image = FileField('Image', validators=[InputRequired(), FileAllowed(images, 'Images only!')])
    order = IntegerField('Order', validators=[InputRequired()])
    is_featured = BooleanField("Is Featured ?")
    parent = QuerySelectField(
        'Parent Category',
        get_label='name',
        allow_blank=True,
        blank_text="No Parent",
        query_factory=lambda: db.session.query(MCategory).filter_by(parent_id=None).order_by('name'))
    submit = SubmitField('Submit')


class MCurrencyForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    symbol = StringField('Symbol', validators=[InputRequired()])
    default = BooleanField('Is Default ?')
    submit = SubmitField('Submit')


class MShippingMethodForm(FlaskForm):
    seller = QuerySelectField(
        'Seller',
        validators=[InputRequired()],
        get_label='full_name',
        query_factory=lambda: db.session.query(User).filter_by(is_seller=True).order_by('first_name'))
    name = StringField('Name', validators=[InputRequired()])
    submit = SubmitField('Submit')


class MProductForm(FlaskForm):
    name = StringField('Product name', validators=[InputRequired(), Length(1, 64)])
    images = MultipleFileField('Product Images', validators=[InputRequired(), FileAllowed(images, 'Images only!')])
    description = TextAreaField('Description', [InputRequired()])
    categories = QuerySelectMultipleField(
        'Categories',
        validators=[InputRequired()],
        get_label='name',
        query_factory=lambda: db.session.query(MCategory).order_by('order'))
    availability = BooleanField(u'Is it currently available?')
    min_order_quantity = IntegerField('Min number of units per order e.g 1', default=1)
    length = FloatField('Length in numbers only e.g 0.99')
    weight = FloatField('Weight in numbers only e.g 0.21')
    height = FloatField('Height in numbers only e.g 10')
    price = FloatField('Price, Figures only e.g 16.99')
    seller = QuerySelectField(
        'Seller',
        validators=[InputRequired()],
        get_label='full_name',
        query_factory=lambda: db.session.query(User).filter_by(is_seller=True).order_by('first_name'))
    price_currency = QuerySelectField(
        'Price currency',
        validators=[InputRequired()],
        get_label='name',
        query_factory=lambda: db.session.query(MCurrency).order_by('name'))
    is_featured = BooleanField("Is Featured ?")
    lead_time = StringField('Delivery time')
    submit = SubmitField('Submit')



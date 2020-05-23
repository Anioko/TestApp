from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import Length, Required

class OpportunityForm(FlaskForm):    
###Public Resumes for professionals
    opportunity_name = StringField(' Name of the organization')
    opportunity_summary = StringField(' Write a very short sentence')
    role_one = StringField('Type of role')
    role_description_one = TextAreaField('Description')
    start_date_one = DateField('Start  Date:', format='%Y/%m/%d', validators=[Optional()])
    end_date_one = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    currently_one = SelectField(u'Currently', choices=[('Yes', 'No')])
    location_city_one = StringField('City')
    location_state_one = StringField('State')
    location_country_one = StringField('Country')
    save = SubmitField('Submit')


class ContractorForm(FlaskForm):    
###Form for 
    contract_name = StringField(' Name of the organization')
    contract_summary = StringField(' Write a very short sentence')
    role_one = StringField('Type of role')
    role_description_one = TextAreaField('Description')
    available_now = SelectField(u'Available now or later', choices=[('Available', 'Available'), ('Available', 'Available')])
    start_date = DateField('Start  Date:', format='%Y/%m/%d', validators=[Optional()])
    end_date = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    location_type = SelectField(u'Onsite or Remote', choices=[('Onsite', 'Onsite'), ('Remote', 'Remote')])
    contract_city = StringField('City')
    contract_state = StringField('State')
    contract_country = StringField('Country')
    currencies = SelectField(u'Select Currency', choices=[
                              ('Albania Lek', 'ALL'),
                              ('Afghanistan Afghani', 'AFN'),
                              ('Argentina Peso', 'ARS'),
                              ('Aruba Guilder', 'AWG'),
                              ('Australia Dollar', 'AUD'),
                              ('Azerbaijan New Manat', 'AZN'),
                              ('Bahamas Dollar', 'BSD'),
                              ('Barbados Dollar', 'BBD'),
                              ('Belarus Ruble', 'BYN'),
                              ('Belize Dollar', 'BZD'),
                              ('Bermuda Dollar', 'BMD'),
                              ('Bolivia Bolíviano', 'BOB'),
                              ('Bosnia and Herzegovina Convertible Marka', 'BAM'),
                              ('Botswana Pula', 'BWP'),
                              ('Bulgaria Lev', 'BGN'),
                              ('Brazil Real', 'BRL'),
                              ('Brunei Darussalam Dollar', 'BND'),
                              ('Cambodia Riel', 'KHR'),
                              ('Canada Dollar', 'CAD'),
                              ('Cayman Islands Dollar', 'KYD'),
                              ('Chile Peso', 'CLP'),
                              ('China Yuan Renminbi', 'CNY'),
                              ('Colombia Peso', 'COP'),
                              ('Costa Rica Colon', 'CRC'),
                              ('Croatia Kuna', 'HRK'),
                              ('Cuba Peso', 'CUP'),
                              ('Czech Republic Koruna', 'CZK'),
                              ('Denmark Krone', 'DKK'),
                              ('Dominican Republic Peso', 'DOP'),
                              ('East Caribbean Dollar', 'XCD'),
                              ('Egypt Pound', 'EGP'),
                              ('El Salvador Colon', 'SVC'),
                              ('Euro Member Countries', 'EUR'),
                              ('Falkland Islands (Malvinas) Pound', 'FKP'),
                              ('Fiji Dollar', 'FJD'),
                              ('Ghana Cedi', 'GHS'),
                              ('Gibraltar Pound', 'GIP'),
                              ('Guatemala Quetzal', 'GTQ'),
                              ('Guernsey Pound', 'GGP'),
                              ('Guyana Dollar', 'GYD'),
                              ('Honduras Lempira', 'HNL'),
                              ('Hong Kong Dollar', 'HKD'),
                              ('Hungary Forint', 'HUF'),
                              ('Iceland Krona', 'ISK'),
                              ('India Rupee', 'INR'),
                              ('Indonesia Rupiah', 'IDR'),
                              ('Iran Rial', 'IRR'),
                              ('Isle of Man Pound', 'IMP'),
                              ('Israel Shekel', 'ILS'),
                              ('Jamaica Dollar', 'JMD'),
                              ('Japan Yen', 'JPY'),
                              ('Jersey Pound', 'JEP'),
                              ('Kazakhstan Tenge', 'KZT'),
                              ('Korea (North) Won', 'KPW'),
                              ('Korea (South) Won', 'KRW'),
                              ('Kyrgyzstan Som', 'KGS'),
                              ('Laos Kip', 'LAK'),
                              ('Lebanon Pound', 'LBP'),
                              ('Liberia Dollar', 'LRD'),
                              ('Macedonia Denar', 'MKD'),
                              ('Malaysia Ringgit', 'MYR'),
                              ('Mauritius Rupee', 'MUR'),
                              ('Mexico Peso', 'MXN'),
                              ('Mongolia Tughrik', 'MNT'),
                              ('Mozambique Metical', 'MZN'),
                              ('Namibia Dollar', 'NAD'),
                              ('Nepal Rupee', 'NPR'),
                              ('Netherlands Antilles Guilder', 'ANG'),
                              ('New Zealand Dollar', 'NZD'),
                              ('Nicaragua Cordoba', 'NIO'),
                              ('Nigeria Naira', 'NGN'),
                              ('Korea (North) Won', 'KPW'),
                              ('Norway Krone', 'NOK'),
                              ('Oman Rial', 'OMR'),
                              ('Pakistan Rupee', 'PKR'),
                              ('Panama Balboa', 'PAB'),
                              ('Paraguay Guarani', 'PYG'),
                              ('Peru Sol', 'PEN'),
                              ('Philippines Peso', 'PHP'),
                              ('Poland Zloty', 'PLN'),
                              ('Qatar Riyal', 'QAR'),
                              ('Romania New Leu', 'RON'),
                              ('Russia Ruble', 'RUB'),
                              ('Saint Helena Pound', 'SHP'),
                              ('Saudi Arabia Riyal', 'SAR'),
                              ('Serbia Dinar', 'RSD'),
                              ('Seychelles Rupee', 'SCR'),
                              ('Singapore Dollar', 'SGD'),
                              ('Solomon Islands Dollar', 'SBD'),
                              ('Somalia Shilling', 'SOS'),
                              ('South Africa Rand', 'ZAR'),
                              ('Korea (South) Won', 'KRW'),
                              ('Sri Lanka Rupee', 'LKR'),
                              ('Sweden Krona', 'SEK'),
                              ('Switzerland Franc', 'CHF'),
                              ('Suriname Dollar', 'SRD'),
                              ('Syria Pound', 'SYP'),
                              ('Taiwan New Dollar', 'TWD'),
                              ('Thailand Baht', 'THB'),
                              ('Trinidad and Tobago Dollar', 'TTD'),
                              ('Turkey Lira', 'TRY'),
                              ('Tuvalu Dollar', 'TVD'),
                              ('Ukraine Hryvnia', 'UAH'),
                              ('United Kingdom Pound', 'GBP'),
                              ('United States Dollar', 'USD'),
                              ('Uruguay Peso', 'UYU'),
                              ('Uzbekistan Som', 'UZS'),
                              ('Venezuela Bolivar', 'VEF'),
                              ('Viet Nam Dong', 'VND'),
                              ('Yemen Rial', 'YER'),
                              ('Zimbabwe Dollar', 'ZWD')])
    save = SubmitField('Submit')


class ResumeForm(FlaskForm):    
###Public Resumes for professionals
    organization_name_one = StringField(' Name of the organization')
    organization_summary_one = StringField(' Write a very short sentence')
    role_one = StringField('Type of role')
    role_description_one = TextAreaField('Description')
    start_date_one = DateField('Start  Date:', format='%Y/%m/%d', validators=[Optional()])
    end_date_one = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    currently_one = SelectField(u'Currently', choices=[('Yes', 'No')])
    location_city_one = StringField('City')
    location_state_one = StringField('State')
    location_country_one = StringField('Country')

    organization_name_two = StringField(' Name of the organization')
    organization_summary_two = StringField(' Write a very short sentence')
    role_two = StringField('Type of role')
    role_description_two = TextAreaField('Description')
    start_date_two = DateField('Start  Date:', format='%Y/%m/%d', validators=[Optional()])
    end_date_two = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    currently_two = SelectField(u'Currently', choices=[('Yes', 'No')])
    location_city_two = StringField('City')
    location_state_two = StringField('State')
    location_country_two = StringField('Country')
    
    organization_name_three = StringField(' Name of the organization')
    organization_summary_three = StringField(' Write a very short sentence')
    role_three = StringField('Type of role')
    role_description_three = TextAreaField('Description')
    start_date_three = DateField('Start Date:', format='%Y/%m/%d', validators=[Optional()])
    end_date_three = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    currently_three = SelectField(u'Currently', choices=[('Yes', 'No')])
    location_city_three = StringField('City')
    location_state_three = StringField('State')
    location_country_three = StringField('Country')

    organization_name_four = StringField(' Name of the organization')
    organization_summary_four = StringField(' Write a very short sentence')
    role_four = StringField('Type of role')
    role_description_four = TextAreaField('Description')
    start_date_four = DateField('Start Date:', format='%Y/%m/%d', validators=[Optional()])
    end_date_four = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    currently_four = SelectField(u'Currently', choices=[('Yes', 'No')])
    location_city_four = StringField('City')
    location_state_four = StringField('State')
    location_country_four = StringField('Country')

    organization_name_five = StringField(' Name of the organization')
    organization_summary_five = StringField(' Write a very short sentence')
    role_five = StringField('Type of role')
    role_description_five = TextAreaField('Description')
    start_date_five = DateField('Start Date:', format='%Y/%m/%d', validators=[Optional()])
    end_date_five = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    currently_five = SelectField(u'Currently', choices=[('Yes', 'No')])
    location_city_five = StringField('City')
    location_state_five = StringField('State')
    location_country_five = StringField('Country')    

    organization_name_six = StringField(' Name of the organization')
    organization_summary_six = StringField(' Write a very short sentence')
    role_six = StringField('Type of role')
    role_description_six = TextAreaField('Description')
    start_date_six = DateField('Start Date:', format='%Y/%m/%d', validators=[Optional()])
    end_date_six = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    currently_six = SelectField(u'Currently', choices=[('Yes', 'No')])
    location_city_six = StringField('City')
    location_state_six = StringField('State')
    location_country_six = StringField('Country')

    school_name_one = StringField(' Name of the school')
    degree_description_one = StringField('Bsc, Msc etc')
    grading_one = StringField('Your grade')
    school_start_date_one = DateField('Start Date:', format='%Y/%m/%d', validators=[Optional()])
    school_end_date_one = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    school_currently_one = SelectField(u'Currently studying', choices=[('Yes', 'No')])
    state_school_one = StringField('City')
    city_school_one = StringField('State')
    country_school_one = StringField('Country')

    school_name_two = StringField(' Name of the school')
    degree_description_two = StringField(' Bsc, Msc etc')
    grading_two = StringField('Your grade')
    school_start_date_two = DateField('Start Date:', format='%Y/%m/%d', validators=[Optional()])
    school_end_date_two = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    school_currently_two = SelectField(u'Currently studying', choices=[('Yes', 'No')])
    state_school_two = StringField('City')
    city_school_two = StringField('State')
    country_school_two = StringField('Country')

    school_name_three = StringField(' Name of the school')
    degree_description_three = StringField(' Bsc, Msc etc')
    grading_three = StringField('Your grade')
    school_start_date_three = DateField('Start Date:', format='%Y/%m/%d', validators=[Optional()])
    school_end_date_three = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    school_currently_three = SelectField(u'Currently studying', choices=[('Yes', 'No')])
    state_school_three = StringField('City')
    city_school_three = StringField('State')
    country_school_three = StringField('Country')

    school_name_four = StringField(' Name of the school')
    degree_description_four = StringField(' Bsc, Msc etc')
    grading_four = StringField(' ')
    school_start_date_four = DateField('Start Date:', format='%Y/%m/%d', validators=[Optional()])
    school_end_date_four = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    school_currently_four = SelectField(u'Currently studying', choices=[('Yes', 'No')])
    state_school_four = StringField('City')
    city_school_four = StringField('State')
    country_school_four = StringField('Country')

    school_name_five = StringField(' Name of the school')
    degree_description_five = StringField(' Bsc, Msc etc')
    grading_five = StringField('Your grade')
    school_start_date_five = DateField('Start Date:', format='%Y/%m/%d', validators=[Optional()])
    school_end_date_five = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    school_currently_five = SelectField(u'Currently studying', choices=[('Yes', 'No')])
    state_school_five = StringField('City')
    city_school_five = StringField('State')
    country_school_five = StringField('Country')
    save = SubmitField('Submit')

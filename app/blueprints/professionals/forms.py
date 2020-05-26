from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.validators import Length, Required

class OpportunityForm(FlaskForm):    
###Opportunity form for both contractors and employment seekers to fill out
    title = StringField(' Title for what you are looking for')
    summary = StringField(' Write a very short summary')
    opportunity_type = SelectField(u'Contractor or Full Time Employment', choices=[('Yes', 'No')])
    available_now = SelectField(u'Available now or later', choices=[('Available', 'Available'), ('Available', 'Available')])
    location_type = SelectField(u'Onsite or Remote', choices=[('Onsite', 'Onsite'), ('Remote', 'Remote')])
    city = StringField('Which City?')
    state = StringField('Which State?')
    country = StringField('Which Country?')
    save = SubmitField('Submit')

class EmploymentForm(FlaskForm):    
###Form for employeees to fill out
    minimum_pay = IntegerField(' Min. pay e.g 1000')
    maximum_pay = IntegerField(' Max. pay e.g 2000')
    minimum_duration = SelectField(u'Min. contract duration in months', choices=[('One', 'One'), 
			      ('Two', 'Two'),
			      ('Three', 'Three'),
			      ('Four', 'Four'),
			      ('Five', 'Five'),
			      ('Six', 'Six'),
			      ('Seven', 'Seven'),
			      ('Eight', 'Eight'),
			      ('Nine', 'Nine'),
			      ('Ten', 'Ten'),
			      ('Eleven', 'Eleven'),
			      ('Twelve', 'Twelve')
			      ('More', 'More')])
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


class ContractorForm(FlaskForm):    
###Form for contractors to fill out
    start_date = DateField('Start  Date:', format='%Y/%m/%d', validators=[Optional()])
    end_date = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    minimum_rate = IntegerField(' Min. hourly rate e.g 500')
    maximum_rate = IntegerField(' Max. hourly rate e.g 500')
    minimum_duration = SelectField(u'Min. contract duration in months', choices=[('One', 'One'), 
			      ('Two', 'Two'),
			      ('Three', 'Three'),
			      ('Four', 'Four'),
			      ('Five', 'Five'),
			      ('Six', 'Six'),
			      ('Seven', 'Seven'),
			      ('Eight', 'Eight'),
			      ('Nine', 'Nine'),
			      ('Ten', 'Ten'),
			      ('Eleven', 'Eleven'),
			      ('Twelve', 'Twelve')
			      ('More', 'More')])
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


class WorkplaceForm(FlaskForm):    
###Form to add workpace by professionals (Employees and contractors)
    name = StringField(' Name of the organization')
    description = StringField(' Write a very short sentence')
    role = StringField('Type of role')
    role_description = TextAreaField('Description')
    start_date = DateField('Start  Date:', format='%Y/%m/%d', validators=[Optional()])
    end_date = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    currently = SelectField(u'Currently', choices=[('Yes', 'Yes'),('No', 'No') ])
    city = StringField('City')
    state = StringField('State')
    country = StringField('Country')
    save = SubmitField('Submit')

class SchoolForm(FlaskForm):    
###Form to add schools attended by professionals (Employees and contractors)
    name_five = StringField(' Name of the school')
    description = StringField(' Bsc, Msc etc')
    grading = StringField('Your grade')
    start_date = DateField('Start Date:', format='%Y/%m/%d', validators=[Optional()])
    end_date = DateField('End Date:', format='%Y/%m/%d', validators=[Optional()])
    currently = SelectField(u'Currently studying', choices=[('Yes', 'Yes'),('No', 'No') ])
    state = StringField('City')
    city = StringField('State')
    country = StringField('Country')
    save = SubmitField('Submit')

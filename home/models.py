from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

from django.core.mail import send_mail


# Create your models here.

# class User(AbstractUser):
#     country = models.CharField(max_length=100, null=True, default=None)
COUNTRIES = (
    ('AD',('Andorra')),
    ('AE',('United Arab Emirates')),
    ('AF',('Afghanistan')),
    ('AG',('Antigua & Barbuda')),
    ('AI',('Anguilla')),
    ('AL',('Albania')),
    ('AM',('Armenia')),
    ('AN',('Netherlands Antilles')),
    ('AO',('Angola')),
    ('AQ',('Antarctica')),
    ('AR',('Argentina')),
    ('AS',('American Samoa')),
    ('AT',('Austria')),
    ('AU',('Australia')),
    ('AW',('Aruba')),
    ('AZ',('Azerbaijan')),
    ('BA',('Bosnia and Herzegovina')),
    ('BB',('Barbados')),
    ('BD',('Bangladesh')),
    ('BE',('Belgium')),
    ('BF',('Burkina Faso')),
    ('BG',('Bulgaria')),
    ('BH',('Bahrain')),
    ('BI',('Burundi')),
    ('BJ',('Benin')),
    ('BM',('Bermuda')),
    ('BN',('Brunei Darussalam')),
    ('BO',('Bolivia')),
    ('BR',('Brazil')),
    ('BS',('Bahama')),
    ('BT',('Bhutan')),
    ('BV',('Bouvet Island')),
    ('BW',('Botswana')),
    ('BY',('Belarus')),
    ('BZ',('Belize')),
    ('CA',('Canada')),
    ('CC',('Cocos (Keeling) Islands')),
    ('CF',('Central African Republic')),
    ('CG',('Congo')),
    ('CH',('Switzerland')),
    ('CI',('Ivory Coast')),
    ('CK',('Cook Iislands')),
    ('CL',('Chile')),
    ('CM',('Cameroon')),
    ('CN',('China')),
    ('CO',('Colombia')),
    ('CR',('Costa Rica')),
    ('CU',('Cuba')),
    ('CV',('Cape Verde')),
    ('CX',('Christmas Island')),
    ('CY',('Cyprus')),
    ('CZ',('Czech Republic')),
    ('DE',('Germany')),
    ('DJ',('Djibouti')),
    ('DK',('Denmark')),
    ('DM',('Dominica')),
    ('DO',('Dominican Republic')),
    ('DZ',('Algeria')),
    ('EC',('Ecuador')),
    ('EE',('Estonia')),
    ('EG',('Egypt')),
    ('EH',('Western Sahara')),
    ('ER',('Eritrea')),
    ('ES',('Spain')),
    ('ET',('Ethiopia')),
    ('FI',('Finland')),
    ('FJ',('Fiji')),
    ('FK',('Falkland Islands (Malvinas)')),
    ('FM',('Micronesia')),
    ('FO',('Faroe Islands')),
    ('FR',('France')),
    ('FX',('France, Metropolitan')),
    ('GA',('Gabon')),
    ('GB',('United Kingdom (Great Britain)')),
    ('GD',('Grenada')),
    ('GE',('Georgia')),
    ('GF',('French Guiana')),
    ('GH',('Ghana')),
    ('GI',('Gibraltar')),
    ('GL',('Greenland')),
    ('GM',('Gambia')),
    ('GN',('Guinea')),
    ('GP',('Guadeloupe')),
    ('GQ',('Equatorial Guinea')),
    ('GR',('Greece')),
    ('GS',('South Georgia and the South Sandwich Islands')),
    ('GT',('Guatemala')),
    ('GU',('Guam')),
    ('GW',('Guinea-Bissau')),
    ('GY',('Guyana')),
    ('HK',('Hong Kong')),
    ('HM',('Heard & McDonald Islands')),
    ('HN',('Honduras')),
    ('HR',('Croatia')),
    ('HT',('Haiti')),
    ('HU',('Hungary')),
    ('ID',('Indonesia')),
    ('IE',('Ireland')),
    ('IL',('Israel')),
    ('IN',('India')),
    ('IO',('British Indian Ocean Territory')),
    ('IQ',('Iraq')),
    ('IR',('Islamic Republic of Iran')),
    ('IS',('Iceland')),
    ('IT',('Italy')),
    ('JM',('Jamaica')),
    ('JO',('Jordan')),
    ('JP',('Japan')),
    ('KE',('Kenya')),
    ('KG',('Kyrgyzstan')),
    ('KH',('Cambodia')),
    ('KI',('Kiribati')),
    ('KM',('Comoros')),
    ('KN',('St. Kitts and Nevis')),
    ('KP',('Korea, Democratic People\'s Republic of')),
    ('KR',('Korea, Republic of')),
    ('KW',('Kuwait')),
    ('KY',('Cayman Islands')),
    ('KZ',('Kazakhstan')),
    ('LA',('Lao People\'s Democratic Republic')),
    ('LB',('Lebanon')),
    ('LC',('Saint Lucia')),
    ('LI',('Liechtenstein')),
    ('LK',('Sri Lanka')),
    ('LR',('Liberia')),
    ('LS',('Lesotho')),
    ('LT',('Lithuania')),
    ('LU',('Luxembourg')),
    ('LV',('Latvia')),
    ('LY',('Libyan Arab Jamahiriya')),
    ('MA',('Morocco')),
    ('MC',('Monaco')),
    ('MD',('Moldova, Republic of')),
    ('MG',('Madagascar')),
    ('MH',('Marshall Islands')),
    ('ML',('Mali')),
    ('MN',('Mongolia')),
    ('MM',('Myanmar')),
    ('MO',('Macau')),
    ('MP',('Northern Mariana Islands')),
    ('MQ',('Martinique')),
    ('MR',('Mauritania')),
    ('MS',('Monserrat')),
    ('MT',('Malta')),
    ('MU',('Mauritius')),
    ('MV',('Maldives')),
    ('MW',('Malawi')),
    ('MX',('Mexico')),
    ('MY',('Malaysia')),
    ('MZ',('Mozambique')),
    ('NA',('Namibia')),
    ('NC',('New Caledonia')),
    ('NE',('Niger')),
    ('NF',('Norfolk Island')),
    ('NG',('Nigeria')),
    ('NI',('Nicaragua')),
    ('NL',('Netherlands')),
    ('NO',('Norway')),
    ('NP',('Nepal')),
    ('NR',('Nauru')),
    ('NU',('Niue')),
    ('NZ',('New Zealand')),
    ('OM',('Oman')),
    ('PA',('Panama')),
    ('PE',('Peru')),
    ('PF',('French Polynesia')),
    ('PG',('Papua New Guinea')),
    ('PH',('Philippines')),
    ('PK',('Pakistan')),
    ('PL',('Poland')),
    ('PM',('St. Pierre & Miquelon')),
    ('PN',('Pitcairn')),
    ('PR',('Puerto Rico')),
    ('PT',('Portugal')),
    ('PW',('Palau')),
    ('PY',('Paraguay')),
    ('QA',('Qatar')),
    ('RE',('Reunion')),
    ('RO',('Romania')),
    ('RU',('Russian Federation')),
    ('RW',('Rwanda')),
    ('SA',('Saudi Arabia')),
    ('SB',('Solomon Islands')),
    ('SC',('Seychelles')),
    ('SD',('Sudan')),
    ('SE',('Sweden')),
    ('SG',('Singapore')),
    ('SH',('St. Helena')),
    ('SI',('Slovenia')),
    ('SJ',('Svalbard & Jan Mayen Islands')),
    ('SK',('Slovakia')),
    ('SL',('Sierra Leone')),
    ('SM',('San Marino')),
    ('SN',('Senegal')),
    ('SO',('Somalia')),
    ('SR',('Suriname')),
    ('ST',('Sao Tome & Principe')),
    ('SV',('El Salvador')),
    ('SY',('Syrian Arab Republic')),
    ('SZ',('Swaziland')),
    ('TC',('Turks & Caicos Islands')),
    ('TD',('Chad')),
    ('TF',('French Southern Territories')),
    ('TG',('Togo')),
    ('TH',('Thailand')),
    ('TJ',('Tajikistan')),
    ('TK',('Tokelau')),
    ('TM',('Turkmenistan')),
    ('TN',('Tunisia')),
    ('TO',('Tonga')),
    ('TP',('East Timor')),
    ('TR',('Turkey')),
    ('TT',('Trinidad & Tobago')),
    ('TV',('Tuvalu')),
    ('TW',('Taiwan, Province of China')),
    ('TZ',('Tanzania, United Republic of')),
    ('UA',('Ukraine')),
    ('UG',('Uganda')),
    ('UM',('United States Minor Outlying Islands')),
    ('US',('United States of America')),
    ('UY',('Uruguay')),
    ('UZ',('Uzbekistan')),
    ('VA',('Vatican City State (Holy See)')),
    ('VC',('St. Vincent & the Grenadines')),
    ('VE',('Venezuela')),
    ('VG',('British Virgin Islands')),
    ('VI',('United States Virgin Islands')),
    ('VN',('Viet Nam')),
    ('VU',('Vanuatu')),
    ('WF',('Wallis & Futuna Islands')),
    ('WS',('Samoa')),
    ('YE',('Yemen')),
    ('YT',('Mayotte')),
    ('YU',('Yugoslavia')),
    ('ZA',('South Africa')),
    ('ZM',('Zambia')),
    ('ZR',('Zaire')),
    ('ZW',('Zimbabwe')),
    ('ZZ',('Unknown or unspecified country')),
)
class ProcessFlow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

class Property(models.Model):
    AssetsType = (('commercial','Commercial'),('retailer', 'Retailer'),)
    TAGS = (('RESALE','RESALE'),('FULLY FUNDED', 'FULLY FUNDED'),('New', 'New'))
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=512,default='')
    price = models.CharField(max_length=100,default='')
    tags = models.CharField(max_length=30, choices=TAGS, default='RESALE')
    property_type = models.CharField(max_length=100,default='')
    email = models.EmailField(max_length=100,default='')
    bedrooms = models.CharField(max_length=100,default='')
    bathrooms = models.CharField(max_length=100,default='')
    halls = models.CharField(max_length=100,default='')
    kitchens = models.CharField(max_length=100,default='')
    area = models.CharField(max_length=100,default='')
    property_id = models.CharField(max_length=100,default='')
    year_built = models.CharField(max_length=100,default='')
    contact = models.CharField(max_length=100,default='')
    lot_dimensions = models.CharField(max_length=100,default='')
    deposit_amount = models.CharField(max_length=100,default='')
    is_fav = models.BooleanField(default=False)
    featured_image = models.ImageField(null=True,blank=True,upload_to= 'featured_image')
    featured_image2 = models.ImageField(null=True,blank=True,upload_to= 'featured_image')
    featured_image3 = models.ImageField(null=True,blank=True,upload_to= 'featured_image')
    featured_image4 = models.ImageField(null=True,blank=True,upload_to= 'featured_image')
    featured_image5 = models.ImageField(null=True,blank=True,upload_to= 'featured_image')
    featured_image6 = models.ImageField(null=True,blank=True,upload_to= 'featured_image')
    featured_image7 = models.ImageField(null=True,blank=True,upload_to= 'featured_image')
    featured_image8 = models.ImageField(null=True,blank=True,upload_to= 'featured_image')
    featured_image9 = models.ImageField(null=True,blank=True,upload_to= 'featured_image')
    featured_image10 = models.ImageField(null=True,blank=True,upload_to= 'featured_image')
    images = models.CharField(max_length=512,default=False)
    about_builder = models.CharField(max_length=512,default=False)
    financial = models.CharField(max_length=512,default=False)
    financial_desclaimer = models.CharField(max_length=1000,default=False)
    due_diligence = models.CharField(max_length=512,default=False)
    property_details = models.CharField(max_length=512,default=False)
    updates = models.CharField(max_length=512,default=False)
    doc_reports = models.CharField(max_length=512,default=False)
    location = models.CharField(max_length=512,default=False)
    map_location = models.CharField(max_length=512,default=False)
    location_detail = models.CharField(max_length=1024,default=False)
    localty = models.CharField(max_length=100,default=False)
    storeys = models.CharField(max_length=100,default=False)
    parking = models.CharField(max_length=100,default=False)
    floor_for_sale = models.CharField(max_length=100,default=False)
    parking_ratio = models.CharField(max_length=100,default=False)
    floor_efficiency = models.CharField(max_length=100,default=False)
    fit_outs = models.CharField(max_length=100,default=False)
    total_area = models.CharField(max_length=100,default=False)
    power_area = models.CharField(max_length=100,default=False)
    power_backup = models.CharField(max_length=100,default=False)
    area_of_sale = models.CharField(max_length=100,default=False)
    air_conditioning = models.CharField(max_length=100,default=False)
    purchase_price = models.IntegerField()
    stamp_duty = models.IntegerField()
    brokerage = models.IntegerField()
    legal_fees = models.IntegerField()
    reserves = models.IntegerField()
    highlights = models.CharField(max_length=1000,default=False)
    acquisition = models.CharField(max_length=100,default=False)
    acquisition_frequency = models.CharField(max_length=100,default=False)
    asset_management = models.CharField(max_length=100,default=False)
    asset_management_frequency = models.CharField(max_length=100,default=False)
    expected_irr = models.CharField(max_length=100,default=False)
    asset_risk = models.CharField(max_length=100,default=False)
    expected_holding_period = models.CharField(max_length=100,default=False)
    minimum_investment = models.CharField(max_length=100,default=False)
    funded_member = models.CharField(max_length=100,default=False)
    total_deal_size = models.CharField(max_length=100,default=False)
    total_sft = models.CharField(max_length=100,default=False)
    asset_type = models.CharField(max_length=30, choices=AssetsType, default='commercial')

    #newly added fields after cloning propshare
    price_psf = models.CharField(max_length=100,default='')
    prop_yield = models.CharField(max_length=100,default='')
    return_target = models.CharField(max_length=100,default='')
    funding_status_percent = models.CharField(max_length=100,default='')
    min_investment = models.CharField(max_length=100,default='')
    monthly_rent = models.CharField(max_length=100,default='')
    ownership_percent = models.CharField(max_length=100,default='')
    popup_text = models.TextField(default='')

    min_investment_inr = models.IntegerField(default=0)
    attractive_price = models.IntegerField(default=0)
    rental_yield = models.CharField(max_length=100,default=0)
    yearly_escalation = models.CharField(max_length=100,default=0)
    reny_pr_sf = models.CharField(max_length=100,default=0)
    lease_period = models.CharField(max_length=100,default='5 Years')
    escalation_percent = models.CharField(max_length=100,default=0)
    floor_plan = models.ImageField(null=True,blank=True,upload_to= 'property_floor_plan')

    def __str__(self):
        return self.name
@receiver(post_save, sender=Property)
def send_new_officer_notification_email(sender, instance, created, **kwargs):

    # if a new officer is created, compose and send the email
    if created:
        name = instance.name if instance.name else "no name given"
        subject = 'NAME: {0}'.format(name)
        message = 'A New Property has been added\n'
        message += 'Property Name: ' + name + '\n' 
              
        send_mail(
            subject,
            message,
            'invest@propfrac.com',
            ['invest@propfrac.com', 'jal39@mailinator.com'],
            fail_silently=True,
        )
    

class PropertyPricing(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    title = models.CharField(default='', max_length=100)
    price= models.IntegerField(default=0)

class Comment(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    comment= models.TextField()

class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image =  models.ImageField(null=True,blank=True,upload_to= 'testimonials')
    comments = models.CharField(max_length=512)

class Faq(models.Model):
    FAQTYPE = (
    ('general','GENERAL'),
    ('taxrelated', 'TAX RELATED'),
    ('nri', 'NRI RELATED'),
   
    )
    question = models.CharField(max_length=100)
    answer = models.TextField()
    faqtype = models.CharField(max_length=20, choices=FAQTYPE, default='general')

class Document(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    title= models.CharField(max_length=512)
    description= models.TextField()
    document = models.FileField(upload_to='document')
class Sponsor(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    title= models.CharField(max_length=512)
    location= models.CharField(max_length=100,default=False)
    logo= models.ImageField(null=True,blank=True,upload_to= 'sponsers')
    description= models.TextField()
    experience_title= models.CharField(max_length=512)
    experience_tag= models.CharField(max_length=100)
    experience_description= models.TextField()
    application_overview= models.TextField()
    application_name= models.CharField(max_length=100)
    application_detail= models.TextField()
    document = models.FileField(upload_to='sponsor_document')
class FinancialModal(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    title= models.CharField(max_length=512)
    day0= models.CharField(max_length=100,blank=True)
    year1= models.CharField(max_length=100,blank=True)
    year2= models.CharField(max_length=100,blank=True)
    year3= models.CharField(max_length=100,blank=True)
    year4= models.CharField(max_length=100,blank=True)
    year5= models.CharField(max_length=100,blank=True)
class ProspectusDocument(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    title= models.CharField(max_length=512)
    document = models.FileField(upload_to='prospectus/document')
   


OWNERSHIP = (
    ('individual','INDIVIDUAL'),
    ('company', 'COMPANY TYPE'),
   
)
ACCREDITATION = (
    ('1','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibus lorem a ipsum egestas, a lacinia ligula condimentum.'),
    ('2','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibus lorem a ipsum egestas, a lacinia ligula condimentum.'),
    ('3','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibus lorem a ipsum egestas, a lacinia ligula condimentum.'),
    ('4','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibus lorem a ipsum egestas, a lacinia ligula condimentum.'),
    ('5','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibus lorem a ipsum egestas, a lacinia ligula condimentum.'),
    ('6','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dapibus lorem a ipsum egestas, a lacinia ligula condimentum.'),
   
)
INVESTMENT_EXP = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    
)
PREVOUSLY_INVESTED = (
    ('1','Stocks'),
    ('2','Mutual Funds'),
    ('3','Bonds'),
    ('4','Reits'),
    ('5','Pvt. Equality'),
    ('6','Venture Capital')
)
US_RESIDENT = ((True, 'Yes'), (False, 'No'))
YESORNO = (('1', 'Yes'), ('0', 'No'))
GENDER = (
    ('male','Male'),
    ('female','Female'),
    ('transgender','Transgender'),
)
class Profile(models.Model):
    CHOOSECAT = (
    ('individual','Individual'),
    ('huf','HUF'),
    ('llp','LLP'),
    ('company','Company'),
    ('trust','Trust'),
    ('sole_proprietor','Sole Proprietor')
    )
    CHOOSEPROFILETYPE = (
    ('self','Self'),
    ('father','Father'),
    ('mother','Mother'),
    ('husband','Husband'),
    ('wife','Wife'),
    ('son','Son'),
    ('daughter','Daughter'),
    ('brother','Brother'),
    ('sister','Sister'),
    ('other','Other')
    )
    RESIDENTIALSTATUS = (
    ('resident_indian','Resident Indian'),
    ('nri','Non Resident Indian'),
    ('pio','OCI Card Holder/PIO'),
    ('f_n','Foreign National')
   
    )
    INCOMEDETAILS = (
    ('1','<Rs. 1 L'),
    ('2','Rs. 1-5 L'),
    ('3','Rs. 5-10 L'),
    ('4','Rs. 10-25 L'),
    ('5','Rs. >Rs. 25 L-1 Cr'),
    ('6','Rs >1 Cr'),
   
    )
    EXISTINGINVESTMENT = (
    ('1','<Rs. 25 L'),
    ('2','Rs. 25-50 L'),
    ('3','Rs. 50-75 L'),
    ('4','Rs. 75-100 L'),
    ('5','>Rs. 1 Cr'),
     
    )
    EXISTINGLOAN = (
    ('1','<Rs. 25 L'),
    ('2','Rs. 25-50 L'),
    ('3','Rs. 50-75 L'),
    ('4','Rs. 75-100 L'),
    ('5','>Rs. 1 Cr'),
     
    )
    AIMOFINVEST = (
    ('1','1. Protect my capital with zero risk of loss of capital'),
    ('2','2. Focus on moderate income with low risk of loss of capital'),
    ('3','3. Focus on moderate income and capital growth'),
    ('4','4. Focus on moderate to high income and capital growth'),
    ('5','5. Focus on high levels of income and growth'),
     
    )
    BESTDESCRIBE = (
    ('1','A. Beginner: This is my first ever investment in any product'),
    ('2','B. Intermediate: I have been investing for 3-5 years'),
    ('3','C. Advanced: I have been investing for 5-10 years'),
    ('4','D. Professional: I have been investing regularly for >10 years'),
    
     
    )
    INVESTMENTRISK = (
    ('1','A. 4-6%, Very Low Risk'),
    ('2','B. 6-8%, Low Risk'),
    ('3','C. 8-12%, Moderate Risk'),
    ('4','D. 12-18%, High Risk'),
    ('5','E. >18%, Very High Risk'),
    
     
    )
    INVESTMENTHORIZON = (
    ('1','A. 0-6 months, Short Term'),
    ('2','B. 6 months-3 years, Medium Term'),
    ('3','C. 3-5 years, Long Term'),
    ('4','D. >5 years, Very Long Term'),
    )
    RISKAPPETITE = (
    ('1','A. Zero Risk (1)'),
    ('2','B. Low Risk (5-6)'),
    ('3','C. Moderate Risk (7-9)'),
    ('4','D. High Risk (10)'),
    )
    LIQUIDITYINVESTMENT = (
    ('1','A. Very important, Highly liquid'),
    ('2','B. Moderately important'),
    ('3','C. I am a long term investor'),
 
    )
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    residence_country = models.CharField(max_length=100, choices=COUNTRIES , default='IN')
    ssn = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    doc_proof = models.FileField(upload_to='UserProfile', blank=True)
   
    us_resident = models.BooleanField(choices=US_RESIDENT,default=False)
    ownership_type = models.CharField(max_length=20, choices=OWNERSHIP, default='individual')
    us_citizen = models.CharField(max_length=30, choices=YESORNO,default=1)
    ssn_taxid = models.CharField(max_length=30, choices=YESORNO,default=1)
    custodial_account = models.CharField(max_length=30, choices=YESORNO,default=1)
    accreditation = models.CharField(max_length=30, choices=ACCREDITATION, default=1)
    investment_experience = models.CharField(max_length=30, choices=INVESTMENT_EXP, default=1)
    previously_invested = models.CharField(max_length=30, choices=PREVOUSLY_INVESTED, default=1)

    choose_category = models.CharField(max_length=100, choices=CHOOSECAT, default='individual')
    choose_profile_type = models.CharField(max_length=100, choices=CHOOSEPROFILETYPE, default='self')
    dob = models.DateField(blank=True,default='1950-01-01')
    gender = models.CharField(max_length=100, choices=GENDER, default='male')
    residential_status = models.CharField(max_length=100, choices=RESIDENTIALSTATUS, default='resident_indian')

    income_details = models.CharField(max_length=100, choices=INCOMEDETAILS, default='1')
    existing_investments  = models.CharField(max_length=100, choices=EXISTINGINVESTMENT, default='1')
    existing_loans  = models.CharField(max_length=100, choices=EXISTINGLOAN, default='1')
    aim_of_investing  = models.CharField(max_length=100, choices=AIMOFINVEST, default='1')
    best_describes  = models.CharField(max_length=100, choices=BESTDESCRIBE, default='1')
    investment_risk   = models.CharField(max_length=100, choices=INVESTMENTRISK, default='1')
    investment_horizon   = models.CharField(max_length=100, choices=INVESTMENTHORIZON, default='1')
    risk_appetite   = models.CharField(max_length=100, choices=RISKAPPETITE, default='1')
    liquidity_investments   = models.CharField(max_length=100, choices=LIQUIDITYINVESTMENT, default='1')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class individualKyc(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(blank=True,default='1950-01-01')
    id_proof = models.FileField(null=True,blank=True,upload_to='IndividualKyc')
    line1 = models.CharField(max_length=150)
    line2 = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=150)
    country = models.CharField(max_length=100, choices=COUNTRIES , default='IN')
    address_proof = models.FileField(null=True,blank=True,upload_to='IndividualKyc')

class CompanyKyc(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    social_channels = models.TextField()
    hq = models.CharField(max_length=100)
    team_size = models.CharField(max_length=50)
    home_page = models.CharField(max_length=50)
    source_of_funds = models.CharField(max_length=1000)
    foundedDate = models.DateField()
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country =models.CharField(max_length=100, choices=COUNTRIES , default='IN')
    accredited_doc = models.FileField(null=True,blank=True,upload_to='CompanyKyc')

class WhatUserSay(models.Model):
    SOCIALMEDIA = (('twitter', 'Twitter'), ('facebook', 'Facebook'), ('linkedin','LinkedIn'))
    name = models.CharField(max_length =50)
    post = models.CharField(max_length =100)
    video_url = models.CharField(max_length =250)
    social_media = models.CharField(max_length =50 ,choices=SOCIALMEDIA, default='linkedin')
    photo = models.ImageField(null=True,upload_to= 'whatUserSays')

    

class WhereOurUserWork(models.Model):
    name = models.CharField(max_length =50)
    logo = models.ImageField(null=True,blank=True,upload_to= 'WhereOurUserWork')
    

class Articles(models.Model):
    article_title = models.TextField()
    description = models.TextField()
    fb_link = models.CharField(max_length =100)
    twitter_link = models.CharField(max_length =100)
    linkedin_link = models.CharField(max_length =100)
    created_at = models.DateField()
    created_by = models.CharField(max_length =100)
    creater_profile_pic = models.ImageField(null=True,upload_to= 'article')
    featured_image = models.ImageField(null=True,upload_to= 'article')
    tag1 = models.CharField(max_length =100)
    tag2 = models.CharField(max_length =100,blank=True)
    tag3 = models.CharField(max_length =100,blank=True)
    tag4 = models.CharField(max_length =100,blank=True)
    tag5 = models.CharField(max_length =100,blank=True)
class Webinars(models.Model):
    title = models.TextField()
    description = models.TextField()
    fb_link = models.CharField(max_length =100)
    twitter_link = models.CharField(max_length =100)
    linkedin_link = models.CharField(max_length =100)
    created_at = models.DateField()
    created_by = models.CharField(max_length =100)
    creater_profile_pic = models.ImageField(null=True,upload_to= 'webinar')
    featured_image = models.ImageField(null=True,upload_to= 'webinar')
    tag1 = models.CharField(max_length =100)
    video_url = models.CharField(max_length=500,blank=True)
    video = models.FileField(null=True,blank=True,upload_to= 'webinar')

class MyEarnings(models.Model):
    # for Current tab
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE,default=1)
    other_income = models.CharField(max_length=100,default='')
    capital_appreciation = models.CharField(max_length=100,default='')
    date_of_investment = models.DateField()
    
    prop_type = models.CharField(max_length=100,default='')
    investment_amount = models.CharField(max_length=100,default='')
    monthly = models.CharField(max_length=100,default='')
    cumulative = models.CharField(max_length=100,default='')
    a_return = models.CharField(max_length=100,default='')
    current_valuation = models.CharField(max_length=100,default='')
    b_return = models.CharField(max_length=100,default='')
    a_b_return = models.CharField(max_length=100,default='')
    #total_average = models.CharField(max_length=100,default='')
   

class myEarningBySold(models.Model):
    # for sold tab
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE,default=1)
    property_type = models.CharField(max_length=100,default='')
    date_of_investment = models.DateField()
    invested_amount = models.CharField(max_length=100,default='')
    total_rent_distributed = models.CharField(max_length=100,default='')
    sale_date = models.DateField()
    sale_proceeds = models.CharField(max_length=100,default='')
    profit_on_sale = models.CharField(max_length=100,default='')
    total_return = models.CharField(max_length=100,default='')
    irr = models.CharField(max_length=100,default='')
    molc = models.CharField(max_length=100,default='')
    
YEAR = (('2021','2021'),('2022','2022')) 
MONTH = (('Jan','January'),('Feb','February'),('March','March'),('Apr','April'),('May','May'),('June','June'),('July','July'),('Aug','August'),('Sept','September'),('Oct','October'),('Nov','November'),('Dec','December'))  
class rentDistribution(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    year = models.CharField(max_length=100,default='2021',choices = YEAR)
    month = models.CharField(max_length=100,default='1',choices = MONTH)
    rent_amount = models.CharField(max_length=100,default='0')
    

class Investments(models.Model):
    # for Current tab 
    INVESTMENTTYPE = (
    ('Direct','Direct'),
    ('PDOF','PDOF'),
 
    )
    ASSETCLASS = (
    ('Residencial','Residencial'),
    ('Office','Office'),
 
    )
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE,default=1)
    #properties_invested = models.CharField(max_length=100,default='')
    #average_rental_yield = models.CharField(max_length=100,default='')
    #total_investment = models.CharField(max_length=100,default='',verbose_name ='Investment')
    current_value = models.CharField(max_length=100,default='')
    investment_summary = models.FileField(upload_to='investment')
    date_of_investment = models.DateField()
    
    invesment_amount = models.CharField(max_length=100,default='')
    rental_yield = models.CharField(max_length=100,default='')
    current_monthaly_rent = models.CharField(max_length=100,default='')
    total_distributions = models.CharField(max_length=100,default='')
    prop_type = models.CharField(max_length=100,default='')
    current_status = models.CharField(max_length=100,default='')
    by_location = models.CharField(max_length=100,default='',verbose_name ='Property Location')
    by_investment_type = models.CharField(max_length=100,choices=INVESTMENTTYPE ,default='Direct',verbose_name ='Investment Type')
    by_asset_class = models.CharField(max_length=100,default='Residencial',verbose_name ='Asset Class',choices=ASSETCLASS)
class Overview(models.Model):
    # for Current tab 
    INVESTMENTTYPE = (
    ('Direct','Direct'),
    ('PDOF','PDOF'),
 
    )
    ASSETCLASS = (
    ('Residencial','Residencial'),
    ('Office','Office'),
 
    )
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    properties = models.CharField(max_length=100,default='')
    #total_investment = models.CharField(max_length=100,default='',verbose_name ='Investment')
    current_value = models.CharField(max_length=100,default='')
    total_distributions = models.CharField(max_length=100,default='')
    property_name = models.CharField(max_length=100,default='')
    invesment_amount = models.CharField(max_length=100,default='')
    rental_yield = models.CharField(max_length=100,default='')
    prop_type = models.CharField(max_length=100,default='')
    current_status = models.CharField(max_length=100,default='')
    total_average = models.CharField(max_length=100,default='')
    by_location = models.CharField(max_length=100,default='',verbose_name ='Property Location')
    by_investment_type = models.CharField(max_length=100,choices=INVESTMENTTYPE ,default='Direct',verbose_name ='Investment Type')
    by_asset_class = models.CharField(max_length=100,default='Residencial',verbose_name ='Asset Class',choices=ASSETCLASS)
class Statements(models.Model):
    # for  Statements

    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default='')
    description = models.CharField(max_length=100,default='')
    property_name = models.CharField(max_length=100,default='')
    debit = models.CharField(max_length=100,default='')
    credit = models.CharField(max_length=100,default='')
    action = models.CharField(max_length=100,default='')
    statement = models.FileField(upload_to='statements')

class Tax(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE,default=1)
    financial_year = models.DateField(default='')
    income = models.CharField(max_length=100,default='')
    tds_percents = models.CharField(max_length=100,default='')
    tds = models.CharField(max_length=100,default='')
    net_distribution = models.CharField(max_length=100,default='')
    tds_doc = models.FileField(upload_to='tax')
    tax_description = models.TextField()
    

   
class Poll(models.Model):
      
    title = models.CharField(max_length=100,default='')
    description = models.TextField()

class CallSchedule(models.Model):
    MORNING = (
        ('1','12:00 AM'),
        ('2','01:00 AM'),
        ('3','03:00 AM'),
        ('4','06:00 AM'),
        ('5','08:00 AM'),
        ('6','10:00 AM'),
        
    )
    AFTERNOON = (
        ('7','12:00 PM'),
        ('8','01:00 PM'),
        ('9','02:00 PM'),
        ('10','04:00 PM'),
        ('11','04:30 PM'),
        ('12','05:00 PM'),
        
    )
    EVENING = (
        ('13','06:00 PM'),
        ('14','07:00 PM'),
        ('15','08:00 PM'),
        ('16','09:00 PM'),
        ('17','10:30 PM'),
        ('18','11:00 PM'),
        
    )
    MODEOFCONTACT = (
        ('1','PHONE CALL'),
        ('2','VIA EMAIL'),
       
        
    )
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_amount = models.CharField(max_length=100,default='')
    schedule_date = models.DateField(default='')
    morning_slots =models.CharField(max_length=300, choices=MORNING,blank=True,default=6)
    afternoon_slots =models.CharField(max_length=300, choices=AFTERNOON, blank=True)
    evening_slots =models.CharField(max_length=300, choices=EVENING, blank=True)
    email = models.EmailField(max_length=100,default='')
    phone = models.CharField(max_length=100,default='')
    mode_of_contact = models.CharField(max_length=300, choices=MODEOFCONTACT, default=1)
    notes = models.TextField(default='',blank=True)

   

     

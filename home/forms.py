from django import forms
from home.models import Property,User,Profile,individualKyc,CompanyKyc,CallSchedule
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    #country =  forms.CharField(widget=forms.HiddenInput())
   
  

    class Meta:
        model = User
       
        fields = ( 'username','email', 'password1', 'password2', )
    
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        #user.country = self.cleaned_data["country"]
        if commit:
            user.save()
        return user

class NameForm(forms.ModelForm):
   
   class Meta:  
        model = Property  
        fields = "__all__"  

class LoginForm(forms.Form):
   
  username=forms.CharField()  
  password=forms.CharField(widget=forms.PasswordInput)  

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('existing_investments','existing_loans','aim_of_investing','best_describes','investment_risk','investment_horizon','risk_appetite','liquidity_investments','income_details','dob','residential_status','gender','choose_profile_type','choose_category','residence_country', 'phone',)

class IndividualKycForm(forms.ModelForm):

    class Meta:
        model = individualKyc
        fields = ('user','first_name','last_name','dob','id_proof','line1','line2','city','state','postal_code','country','address_proof')
class CompanyKycForm(forms.ModelForm):

    class Meta:
        model = CompanyKyc
        fields = ('user','name','company','email','social_channels','hq','team_size','home_page','source_of_funds','foundedDate','city','state','country','accredited_doc')
class CallScheduleForm(forms.ModelForm):

    class Meta:
        model = CallSchedule
        fields = ('user','property','investment_amount','schedule_date','morning_slots','afternoon_slots','evening_slots','email','phone','mode_of_contact','notes')

class ContactForm(forms.Form):
        first_name = forms.CharField(max_length = 50)
        last_name = forms.CharField(max_length = 50)
        email_address = forms.EmailField(max_length = 150)
        message = forms.CharField(widget = forms.Textarea, max_length = 2000)
        phone = forms.CharField(max_length = 50)


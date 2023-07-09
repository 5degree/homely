from django.shortcuts import render
from home.models import Property
from home.models import Testimonials,ProcessFlow,WhatUserSay,WhereOurUserWork,Articles,Webinars,MyEarnings,Investments,Overview,Statements,Tax,Poll
from home.models import myEarningBySold,rentDistribution,myEarningBySold,CallSchedule,Faq,FinancialModal,Sponsor,Document,ProspectusDocument,PropertyPricing,individualKyc,CompanyKyc
from pprint import pprint
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
from home.forms import SignUpForm,NameForm,LoginForm,UserForm,ProfileForm,IndividualKycForm,CompanyKycForm,ContactForm,CallScheduleForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db import  transaction
from django.contrib import messages
from django import forms
from .filters import UserFilter
from .filters import PropertyFilter
from django.core.mail import send_mail, BadHeaderError
#from xhtml2pdf import pisa 
#from io import StringIO
from django.template.loader import get_template 
from django.template import Context 
import random


# Create your views here.

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['properties'] = Property.objects.all()
        context['testimonials'] = Testimonials.objects.all()
        context['whatusersays'] = WhatUserSay.objects.all()
        return context


# class ContactView(TemplateView):
#     template_name = "web/contact.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
       
#         return context


class LoginView(TemplateView):
    template_name = "web/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return context

class RegisterView(TemplateView):
    template_name = "web/register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return context

class PropertySingleView(TemplateView):
    template_name = "web/property-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property'] = Property.objects.get(id=self.kwargs['id'])  
        context['related_properties'] = Property.objects.exclude(id=self.kwargs['id'])
        context['property_images'] = context['property'].images.split(",")
        context['financial_modals'] = FinancialModal.objects.raw('SELECT * FROM  home_financialmodal WHERE property_id = %s', [self.kwargs['id']])
        context['sponsors'] = Sponsor.objects.raw('SELECT * FROM  home_sponsor WHERE property_id = %s', [self.kwargs['id']])
        context['documents'] = Document.objects.raw('SELECT * FROM  home_document WHERE property_id = %s', [self.kwargs['id']])
        context['PropertyPricings'] = PropertyPricing.objects.raw('SELECT * FROM  home_propertypricing WHERE property_id = %s', [self.kwargs['id']])

        context['is_call_scheduled'] = CallSchedule.objects.raw('SELECT id FROM  home_callschedule WHERE property_id = {p_id} AND user_id ={u_id} LIMIT 1'.format(u_id=self.request.user.id,p_id=self.kwargs['id']))
        #context['property_graph'] = (context['property'].purchase_price + context['property'].stamp_duty)

        #for PropertyPricing in context['PropertyPricings']:
       
       
        return context



class MyPropertiesView(TemplateView):
    template_name = "web/user-my-properties.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['properties'] = Property.objects.all()

       
        return context

def property_invest(request,prop_id):
    # if this is a POST request we need to process the form data
    property = Property.objects.get(id=prop_id)

     
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CallScheduleForm(request.POST,request.FILES)
        
        # check whether it's valid:
        if form.is_valid():
            form.save()
            #Send Mail to user 
           
            subject = 'Your Call is Scheduled!'
            
            message = "Your call is Scheduled on : "+ str(form.cleaned_data['schedule_date']) +" We Will Contact you! Thanks for showing your Interest"
            
            try:
                send_mail(subject, message, 'invest@propfrac.com', [request.user.email], fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('/propertyAdmin/user-profile')
        else:
            messages.error(request, 'Please correct the error below.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CallScheduleForm()

    return render(request, 'web/call-schedule.html', {'form': form, 'prop_id': prop_id,'property':property})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			'phone':form.cleaned_data['phone'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'invest@propfrac.com', ['invest@propfrac.com'], fail_silently=True) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("/")
      
	form = ContactForm()
	return render(request, "web/contact.html", {'form':form})

def property_listing(request):
   
    if request.GET.get('sort') == 'recent':
        properties = Property.objects.all().order_by('-id')
       
        
    else:
        properties = Property.objects.all()
       
    
    prop_filter = PropertyFilter(request.GET, queryset=properties)


    return render(request, 'web/property-listing.html', {'filter': prop_filter})


class HowItWorksView(TemplateView):
    template_name = "web/how-it-works.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return context

class OptionsView(TemplateView):
    template_name = "web/options.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return context

class WhyfractionalView(TemplateView):
    template_name = "web/why-fractional.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return context

class FaqView(TemplateView):
    template_name = "web/faq.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faqs'] = Faq.objects.all()

       
        return context
class WhyCommercialView(TemplateView):
    template_name = "web/why-commercial.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return context

class PrivateAccessView(TemplateView):
    template_name = "web/private-access.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return context
class KnowladgeCenterView(TemplateView):
    template_name = "web/knowladge-center.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Articles.objects.all()
       
        return context
class WebinarView(TemplateView):
    template_name = "web/webinar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['webinars'] = Webinars.objects.all()
       
        return context

class ArticleSingleView(TemplateView):
    template_name = "web/article-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = Articles.objects.get(id=self.kwargs['id'])  
        context['articles'] = Articles.objects.exclude(id=self.kwargs['id'])
       
       
        return context

class InvestorProfileView(TemplateView):
    template_name = "web/investor-profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['whatusersays'] = WhatUserSay.objects.all()
        context['WhereOurUserWorks'] = WhereOurUserWork.objects.all()
       
        return context
class AboutUsView(TemplateView):
    template_name = "web/about-us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return context
class InsightView(TemplateView):
    template_name = "web/insight.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return context
class TermView(TemplateView):
    template_name = "web/term.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return context
class PrivacyView(TemplateView):
    template_name = "web/privacy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return context
#------------------ Admin View----------------------
class AdminIndexView(TemplateView):
    template_name = "prop_admin/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['properties'] = Property.objects.all()
        context['testimonials'] = Testimonials.objects.all()
        return context
class AdminPropertyListingView(TemplateView):
    template_name = "prop_admin/property_listing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['properties'] = Property.objects.all()

        return context

class AdminUserProfileView(TemplateView):
    template_name = "prop_admin/user-profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['user'] = self.request.user
      

        return context
class AdminProcessFlowChartView(TemplateView):
    template_name = "prop_admin/process_flowchart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flows'] = ProcessFlow.objects.raw('SELECT * FROM  home_processflow WHERE user_id = %s', [self.request.user.id])
      
       

        return context
class AdminProspectusView(TemplateView):
    template_name = "prop_admin/prospectus.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prospectus'] = ProspectusDocument.objects.all()
      

        return context
class AdminKycView(TemplateView):
    template_name = "prop_admin/kyc.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      

        return context


class AdminSecureYourAccountView(TemplateView):
    template_name = "prop_admin/secure_your_account.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      

        return context
class AdminMyEarningsView(TemplateView):
    template_name = "prop_admin/my_earnings.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        #context['myEarnings'] = MyEarnings.objects.raw('SELECT * FROM  home_myearnings WHERE user_id = %s', [self.request.user.id] )
        context['myEarnings'] = MyEarnings.objects.filter(user_id=self.request.user.id).all()
        context['myEarningBySolds'] = myEarningBySold.objects.filter(user_id=self.request.user.id).all()
        
        context['rentDistributions_prop'] = rentDistribution.objects.filter(user_id=self.request.user.id).all()
        context['rentDistributions_Jan'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Jan" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_Feb'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Feb" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_March'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "March" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_Aprl'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Apr" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_May'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "May" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_June'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "June" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_July'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "July" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_Aug'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Aug" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_Sept'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Sept" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_Oct'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Oct" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_Nov'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Nov" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_Dec'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Dec" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        total_earning = total_investment = total_monthly = total_cumulative =  total_a_avrg_return = total_b_avrg_return =total_ab_avrg_return = total_current_valuation = total_a_b_return = total_other_income = total_capital_appreciation =  0
        # variables  for SOLD tab
        return_multiple = sum_of_total_return = total_sale_invested_amount = full_rent_distributed = total_sale_proceeds = total_profit_on_sale = total_molc = average_irr = total_irr = 0
        #variables For Rent Distribution Graph
        dataSet = ''
        prop_name = []
        jan_val = []
        feb_val = []
        march_val = []
        aprl_val = []
        may_val = []
        june_val = []
        july_val = []
        aug_val = []
        sept_val = []
        oct_val = []
        nov_val = []
        dec_val = []
        total_rent = 0

        for total in context['myEarnings']:
           total_investment = total_investment + int(total.investment_amount)
           total_monthly = total_monthly + int(total.monthly)
           total_cumulative = total_cumulative + int(total.cumulative)
           total_current_valuation = total_current_valuation + int(total.current_valuation)
           total_a_avrg_return = total_a_avrg_return + float(total.a_return)
           total_b_avrg_return = total_b_avrg_return + float(total.b_return)
           total_ab_avrg_return = total_ab_avrg_return + float(total.a_b_return)
           total_other_income = total_other_income + float(total.other_income)
           total_capital_appreciation = total_capital_appreciation + float(total.capital_appreciation)

        # calculation for SOLD tab - --------
        for sold in context['myEarningBySolds']:
        
            total_sale_invested_amount = total_sale_invested_amount + float(sold.invested_amount)
            full_rent_distributed = full_rent_distributed + float(sold.total_rent_distributed)
            total_sale_proceeds = total_sale_proceeds + float(sold.sale_proceeds)
            total_profit_on_sale = total_profit_on_sale + float(sold.profit_on_sale)
            total_molc = total_molc + float(sold.molc)
            total_irr = total_irr + float(sold.irr)
            sum_of_total_return = sum_of_total_return + float(sold.total_return)
        
        average_irr = (total_irr) / len(context['myEarningBySolds']) if len(context['myEarningBySolds']) else 0 
        

        #return_multiple = (sum_of_total_return / total_sale_invested_amount) 
        if total_sale_invested_amount != 0:
            return_multiple = sum_of_total_return / total_sale_invested_amount
        else:
            return_multiple = 0

    
        # For Loop Rent Distribution Graph
        for prop in context['rentDistributions_prop']:
            prop_name.append(prop.property.name)if prop.property.name not in prop_name else prop_name
            total_rent = total_rent + int(prop.rent_amount)
       
        for jan in context['rentDistributions_Jan']:
            jan_val.append(int(jan.rent_amount))
        for feb in context['rentDistributions_Feb']:
            feb_val.append(int(feb.rent_amount))
        for march in context['rentDistributions_March']:
            march_val.append(int(march.rent_amount))
        for aprl in context['rentDistributions_Aprl']:
            aprl_val.append(int(aprl.rent_amount))
        for may in context['rentDistributions_May']:
            may_val.append(int(may.rent_amount))
        for june in context['rentDistributions_June']:
            june_val.append(int(june.rent_amount))
        for july in context['rentDistributions_July']:
            july_val.append(int(july.rent_amount))
        for aug in context['rentDistributions_Aug']:
            aug_val.append(int(aug.rent_amount))
        for sept in context['rentDistributions_Sept']:
            sept_val.append(int(sept.rent_amount))
        for oct in context['rentDistributions_Oct']:
            oct_val.append(int(oct.rent_amount))
        for nov in context['rentDistributions_Nov']:
            nov_val.append(int(nov.rent_amount))
        for dec in context['rentDistributions_Dec']:
            dec_val.append(int(dec.rent_amount))
        
        total_earning = total_rent + total_other_income + total_capital_appreciation
        total_ab_avrg_return = (total_ab_avrg_return) / len(context['myEarnings']) if len(context['myEarnings']) else 0   
        context['total_investment'] = total_investment
        context['total_monthly'] = total_monthly
        context['total_cumulative'] = total_cumulative
        context['total_current_valuation'] = total_current_valuation
        context['total_a_avrg_return'] = total_a_avrg_return
        context['total_b_avrg_return'] = total_b_avrg_return
        context['total_ab_avrg_return'] = total_ab_avrg_return
        context['total_other_income'] = total_other_income
        context['total_capital_appreciation'] = total_capital_appreciation
        context['total_earning'] = total_earning
        # Cntext for SOLD tab-------
        context['total_sale_invested_amount'] = total_sale_invested_amount
        context['full_rent_distributed'] = full_rent_distributed
        context['total_sale_proceeds'] = total_sale_proceeds
        context['total_profit_on_sale'] = total_profit_on_sale
        context['total_molc'] = total_molc
        context['average_irr'] = average_irr
        context['sum_of_total_return'] = sum_of_total_return
        context['return_multiple'] = return_multiple

        # data for distribution Graph 

        context['prop_name'] = prop_name
        context['total_rent'] = total_rent
        context['jan_val'] = jan_val
        context['feb_val'] = feb_val
        context['march_val'] = march_val
        context['aprl_val'] = aprl_val
        context['may_val'] = may_val
        context['june_val'] = june_val
        context['july_val'] = july_val
        context['aug_val'] = aug_val
        context['sept_val'] = sept_val
        context['oct_val'] = oct_val
        context['nov_val'] = nov_val
        context['dec_val'] = dec_val

      
        return context
class AdminInvestmentsView(TemplateView):
    template_name = "prop_admin/investments.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['investments'] = Investments.objects.filter(user_id=self.request.user.id).all()

        total_investment = total_current_value = total_distributions =  total_yield = 0
        property_graph = property_val = property_color = rental_yield_color = rental_yield_val= rental_yield_graph =""
        color_arr = ['#346888', '#5886a5', '#7aa6c2', '#9dc6e0' , '#c1e7ff']
        for total in context['investments']:
           total_investment = total_investment + int(total.invesment_amount)
           total_current_value = total_current_value + int(total.current_value)
          
           total_yield = total_yield + float(total.rental_yield)
           # By Property Graph
            
           property_graph =  "'"+ total.property.name +"'," + property_graph
           property_val =  "'"+ "1" +"'," + property_val
           pr = lambda: random.randint(0,255)
           property_color =  "'"+ (random.choice(color_arr)) +"'," + property_color
           # By Rental Yield Graph
           
           rental_yield_graph =  "'"+ total.property.name +"'," + rental_yield_graph
           rental_yield_val =   total.rental_yield +"," + rental_yield_val
           pr = lambda: random.randint(0,255)
           rental_yield_color =  "'"+ (random.choice(color_arr)) +"'," + rental_yield_color
           

        total_yield = (total_yield) / len(context['investments']) if len(context['investments']) else 0   
       
        context['total_investment'] = total_investment
        context['total_current_value'] = total_current_value
        context['total_yield'] = total_yield
        context['property_graph'] = property_graph
        context['property_val'] = property_val
        context['property_color'] = property_color
        context['rental_yield_graph'] = rental_yield_graph
        context['rental_yield_val'] = rental_yield_val
        context['rental_yield_color'] = rental_yield_color
      
        

        return context

        return context
class AdminTaxView(TemplateView):
    template_name = "prop_admin/tax.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
 
        context['tax'] = Tax.objects.filter(user_id=self.request.user.id).first()

        return context
class AdminPollView(TemplateView):
    template_name = "prop_admin/poll.html"

    def get_context_data(self, **kwargs):
      
        context = super().get_context_data(**kwargs)
        context['polls'] = Poll.objects.all()

        return context
class AdminInvestView(TemplateView):
    template_name = "prop_admin/invest.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['properties'] = Property.objects.all()
      

        return context

class AdminDividendView(TemplateView):
    template_name = "prop_admin/dividend.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      

        return context
class AdminOverviewView(TemplateView):
    template_name = "prop_admin/overview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['investments'] = Investments.objects.filter(user_id=self.request.user.id).all()
        #context['overviews'] = Overview.objects.filter(user_id=self.request.user.id).all()

        context['rentDistributions_Jan'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Jan" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_Feb'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Feb" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_March'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "March" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_Aprl'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Apr" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_May'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "May" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_June'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "June" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_July'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "July" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_Aug'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Aug" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_Sept'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Sept" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_Oct'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Oct" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_Nov'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Nov" AND user_id ={u_id} '.format(u_id=self.request.user.id))
        context['rentDistributions_Dec'] = rentDistribution.objects.raw('SELECT id FROM  home_rentdistribution WHERE month = "Dec" AND user_id ={u_id} '.format(u_id=self.request.user.id))
      
        total_investment = current_value = total_distributions =  total_yield = 0
        Location_graph = Location_val = location_color = portfolio_color = portfolio_val= portfolio_graph =""
        direct_investment_graph = pdof_investment_graph = asset_residential_graph = asset_office_graph = 0
        color_arr = ['#346888', '#5886a5', '#7aa6c2', '#9dc6e0' , '#c1e7ff']
        total_dist_graph = []
        jan_val = feb_val = march_val = aprl_val = may_val = june_val = july_val = aug_val = sept_val = oct_val = nov_val = dec_val = 0
        #  For loops for Total disributions - 
        for jan in context['rentDistributions_Jan']:
            jan_val =  int(jan_val) + int(jan.rent_amount)
        
       
        for feb in context['rentDistributions_Feb']:
            feb_val =  int(feb_val) + int(feb.rent_amount)
        for march in context['rentDistributions_March']:
            march_val =  int(march_val) + int(march.rent_amount)
        for aprl in context['rentDistributions_Aprl']:
            aprl_val =  int(aprl_val) + int(aprl.rent_amount)
        for may in context['rentDistributions_May']:
            may_val =  int(may_val) + int(may.rent_amount)
        for june in context['rentDistributions_June']:
            june_val =  int(june_val) + int(june.rent_amount)
        for july in context['rentDistributions_July']:
            july_val =  int(july_val) + int(july.rent_amount)
        for aug in context['rentDistributions_Aug']:
            aug_val =  int(aug_val) + int(aug.rent_amount)
        for sept in context['rentDistributions_Sept']:
            sept_val =  int(sept_val) + int(sept.rent_amount)
        for oct in context['rentDistributions_Oct']:
            oct_val =  int(oct_val) + int(oct.rent_amount)
        for nov in context['rentDistributions_Nov']:
            nov_val =  int(nov_val) + int(nov.rent_amount)
        for dec in context['rentDistributions_Dec']:
            dec_val =  int(dec_val) + int(dec.rent_amount)

        total_dist_graph = [jan_val,feb_val,march_val,aprl_val,may_val,june_val,july_val,aug_val,sept_val,oct_val,nov_val,dec_val]
        total_distributions = jan_val + feb_val + march_val + aprl_val + may_val + june_val + july_val + aug_val + sept_val + oct_val + nov_val + dec_val


        for idx,total in enumerate(context['investments']):
           total_investment = total_investment + int(total.invesment_amount)
           current_value = current_value + int(total.current_value)
           
           total_yield = total_yield + float(total.rental_yield)
           #for Portfolio Graph
           portfolio_graph =  "'"+ total.property.name +"'," + portfolio_graph
           portfolio_val =  "'"+ "1" +"'," + portfolio_val
           pr = lambda: random.randint(1,99)
           
          
           portfolio_color =  "'"+ (random.choice(color_arr)) +"'," + portfolio_color

           #for Location Graph
           Location_graph =  "'"+ total.by_location +"'," + Location_graph
           Location_val =  "'"+ "1" +"'," + Location_val
           r = lambda: random.randint(0,255)
         
           location_color =  "'"+ (random.choice(color_arr)) +"'," + location_color
           #Investment Graph
           if(total.by_investment_type == 'Direct'):
               direct_investment_graph = direct_investment_graph + 1
           else:
               pdof_investment_graph = pdof_investment_graph + 1
            #Asset Class Graph
           if(total.by_asset_class == 'Residencial'):
               asset_residential_graph = asset_residential_graph + 1
           else:
               asset_office_graph = asset_office_graph + 1




          
          
       
        total_yield = (total_yield) / len(context['investments']) if len(context['investments']) else 0
       
        context['total_investment'] = total_investment
        context['current_value'] = current_value
        context['total_distributions'] = total_distributions
        context['total_yield'] = total_yield
        context['Location_graph'] = Location_graph
        context['Location_val'] = Location_val
        context['location_color'] = location_color
        context['portfolio_graph'] = portfolio_graph
        context['portfolio_val'] = portfolio_val
        context['portfolio_color'] = portfolio_color
        context['direct_investment_graph'] = direct_investment_graph
        context['pdof_investment_graph'] = pdof_investment_graph
        context['asset_residential_graph'] = asset_residential_graph
        context['asset_office_graph'] = asset_office_graph
        context['total_dist_graph'] = total_dist_graph
        

        return context

def overviewPdf(request): 
    template = get_template("prop_admin/overview.html") 
    context = {'pagesize':'A4'}
    html = template.render(context) 
    # result = StringIO() 
    # pdf = pisa.pisaDocument(StringIO(html), dest=result) 
    # if not pdf.err: 
    #     return HttpResponse(result.getvalue(), content_type='application/pdf') 
    # else: return HttpResponse('Errors')

class AdminStatementView(TemplateView):
    template_name = "prop_admin/statement.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statement'] = Statements.objects.filter(user_id=self.request.user.id).first()

      

        return context
class AdminTaxView(TemplateView):
    template_name = "prop_admin/tax.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taxes'] = Tax.objects.filter(user_id=self.request.user.id).all()

      

        return context

@login_required
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'prop_admin/propertyManager.html', {'form': form})

def Login2(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],
                                    password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('propertyAdmin/overview')
                else:
                    return HttpResponse('>>>>>>>>>>>Authentication Failed, Please Try Again.<<<<<<<<<<<')
            else:
                return HttpResponse('>>>>>>>>>>>Authentication Failed. Something went wrong.<<<<<<<<<<<')
    else:
        form = LoginForm()
    return render(request,'web/login.html',{'form':form})
def Registeration_agreement(request):
   
   
    return render(request, 'web/registeration_agreement.html')

def Registeration_agreement_get(request):
   country=request.POST['country']
   if country:
       return redirect('register', country=request.POST['country'])
   else:
       return redirect('Investors-register')
       
   
   
def Register(request):
    
      
    if request.method == 'POST': 
        form = SignUpForm(request.POST)
        if form.is_valid():
           
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            subject = "New registration" 
            body = {"Welcome! You have successfully Registered!"}
            message = "\n".join(body)
            try:
                send_mail(subject, message,  'invest@propfrac.com', [form.cleaned_data['email']], fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
				
            return HttpResponseRedirect('/propertyAdmin/overview')
    else:
        form = SignUpForm()
    return render(request, 'web/register.html', {'form': form})


def Logout(request):
    
    logout(request)
    return redirect('/')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('user-profile')
        else:
            messages.error(request, 'Please correct the error below.')
            
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'prop_admin/user-profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
   

@login_required
def AdminKycIndividual(request):
    # if this is a POST request we need to process the form data
    try:
        is_kyc = individualKyc.objects.get(user_id=request.user.id)
    except:
        is_kyc = 'blank'
    
     
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IndividualKycForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Individual KYC was successfully uploaded!')
            return redirect('/kyc')
        else:
            messages.error(request, 'Please correct the error below.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IndividualKycForm()

    return render(request, 'prop_admin/kyc_individual.html', {'form': form, 'is_kyc':is_kyc})
    
@login_required
def AdminKycCompany(request):
    # if this is a POST request we need to process the form data
    try:
        is_kyc = CompanyKyc.objects.get(user_id=request.user.id)
    except:
        is_kyc = 'blank'
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CompanyKycForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Company KYC was successfully uploaded!')
            return redirect('/kyc')
        else:
            messages.error(request, 'Please correct the error below.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CompanyKycForm()

    return render(request, 'prop_admin/kyc_company.html', {'form': form, 'is_kyc':is_kyc})
    

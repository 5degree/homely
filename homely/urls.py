"""homely URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.contrib.auth.decorators import login_required
from home.views import  IndexView

from home.views import LoginView
from home.views import RegisterView
from home.views import PropertySingleView
from home.views import MyPropertiesView
from home.views import HowItWorksView
from home.views import OptionsView
from home.views import WhyfractionalView
from home.views import WhyCommercialView
from home.views import FaqView
from home.views import KnowladgeCenterView
from home.views import AboutUsView
from home.views import InsightView
from home.views import TermView
from home.views import PrivacyView
from home.views import Login2,Register,Logout
 #Route for admin templates

from home.views import AdminIndexView
# from home.views import PropertyManagerView
from home.views import overviewPdf,property_invest,AdminPollView,AdminTaxView,AdminStatementView,PrivateAccessView,WebinarView,ArticleSingleView,InvestorProfileView,contact,Registeration_agreement,Registeration_agreement_get,update_profile,get_name,property_listing,AdminPropertyListingView,AdminUserProfileView,AdminProcessFlowChartView,AdminProspectusView,AdminKycView,AdminKycIndividual,AdminKycCompany,AdminSecureYourAccountView,AdminMyEarningsView,AdminInvestmentsView,AdminTaxView,AdminInvestView,AdminDividendView,AdminOverviewView



admin.site.site_header ="Homely Admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name='ss'),
    
    path('login',Login2,name='login'),
    path('logout',Logout,name='logout'),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    path('Investors-register',Registeration_agreement,name='Investors-register'),
    #path('Investors-register-get/$',Registeration_agreement_get,name='Investors-register-get'),
    # path('register/(?P<country>\d+)/$',Register,name='register'),
    path('register',Register,name='register'),
   

    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name="password_reset_complete"),

 
    re_path(r'^property-listing/$',property_listing,name='property-listing'),
    re_path(r'^contact',contact,name='contact'),
    re_path(r'^property-invest/(?P<prop_id>\d+)/',login_required(property_invest),name='property_invest'),

    path('property-single/<int:id>',login_required(PropertySingleView.as_view()),name='property-single'),
    
    path('user-MyProperties',login_required(MyPropertiesView.as_view()),name='user-MyProperties'),

    path('how-it-works',HowItWorksView.as_view(),name='how-it-works'),
    path('options',OptionsView.as_view(),name='options'),
    path('why-fractional',WhyfractionalView.as_view(),name='why-fractional'),
    path('why-commercial',WhyCommercialView.as_view(),name='why-commercial'),
    path('private-access',PrivateAccessView.as_view(),name='private-access'),
    path('faq',FaqView.as_view(),name='faq'),
    path('webinar',WebinarView.as_view(),name='webinar'),
    path('knowladge-center',KnowladgeCenterView.as_view(),name='knowladge-center'),
    path('article/<int:id>',ArticleSingleView.as_view(),name='article'),
    path('investor-profile',InvestorProfileView.as_view(),name='investor-profile'),
    path('about-us',AboutUsView.as_view(),name='about-us'),
    path('insight',InsightView.as_view(),name='insight'),
    path('term',TermView.as_view(),name='term'),
    path('privacy',PrivacyView.as_view(),name='privacy'),
    #Route for admin templates
    path('propertyAdmin/',login_required(AdminIndexView.as_view()),name='propertyAdmin'),
    path('propertyAdmin/property-manager',get_name,name='property-manager'),#
    path('propertyAdmin/property-list',login_required(AdminPropertyListingView.as_view()),name='property-list'),
    path('propertyAdmin/user-profile',update_profile,name='user-profile'),
    path('propertyAdmin/process-flow-chart',login_required(AdminProcessFlowChartView.as_view()),name='/process-flow-chart'),
    path('propertyAdmin/prospectus',login_required(AdminProspectusView.as_view()),name='/prospectus'),
    path('propertyAdmin/kyc',login_required(AdminKycView.as_view()),name='/kyc'),
    path('propertyAdmin/kyc-individual',AdminKycIndividual,name='/kyc-individual'),
    path('propertyAdmin/kyc-company',AdminKycCompany,name='/kyc-company'),
    path('propertyAdmin/secure-your-account',login_required(AdminSecureYourAccountView.as_view()),name='/secure-your-account'),
    path('propertyAdmin/my-earnings',login_required(AdminMyEarningsView.as_view()),name='/my-earnings'),
    path('propertyAdmin/investments',login_required(AdminInvestmentsView.as_view()),name='/investments'),
    path('propertyAdmin/tax',login_required(AdminTaxView.as_view()),name='/tax'),
    path('propertyAdmin/invest',login_required(AdminInvestView.as_view()),name='/invest'),
    path('propertyAdmin/dividend',login_required(AdminDividendView.as_view()),name='/dividend'),
    path('propertyAdmin/overview',login_required(AdminOverviewView.as_view()),name='/overview'),
    path('propertyAdmin/overview-pdf',login_required(overviewPdf),name='/overview-pdf'),
    path('propertyAdmin/statements',login_required(AdminStatementView.as_view()),name='/statements'),
    path('propertyAdmin/polls',login_required(AdminPollView.as_view()),name='/polls'),
   
  

]   
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)



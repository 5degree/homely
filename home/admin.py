from django.contrib import admin
from home.models import rentDistribution,myEarningBySold,CallSchedule,PropertyPricing,Poll,Tax,Statements,Overview,Investments,MyEarnings,Webinars,Articles,WhereOurUserWork,WhatUserSay,ProcessFlow,Property,Document,Testimonials,Faq,Sponsor,FinancialModal,Profile,ProspectusDocument,individualKyc,CompanyKyc, CustomUser

class UserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone', 'is_staff' ]

admin.site.register(Property)
admin.site.register(Testimonials)
admin.site.register(Faq)
admin.site.register(Document)
admin.site.register(Sponsor)
admin.site.register(FinancialModal)
admin.site.register(Profile)
admin.site.register(ProspectusDocument)
admin.site.register(individualKyc)
admin.site.register(CompanyKyc)
admin.site.register(ProcessFlow)
admin.site.register(WhatUserSay)
admin.site.register(WhereOurUserWork)
admin.site.register(Articles)
admin.site.register(Webinars)
admin.site.register(MyEarnings)
admin.site.register(Investments)
#admin.site.register(Overview)
admin.site.register(Statements)
admin.site.register(Tax)
admin.site.register(Poll)
admin.site.register(PropertyPricing)
admin.site.register(CallSchedule)
admin.site.register(myEarningBySold)
admin.site.register(rentDistribution)
admin.site.register(CustomUser, UserAdmin)

# Register your models here.


from django.contrib import admin

from barkasse.models import Transaction, Shop, Account, Household, Member

admin.site.register(Household)
admin.site.register(Member)


from barkasse.models import Transaction, Shop, Account, Household, Member
from barkasse.household import HHListView, HHCreateView, HHUpdateView, HHDeleteView

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin


class HouseholdList(LoginRequiredMixin, generic.ListView):
    model = Household

    def get_queryset(self):
        return Household.objects.filter(member__user__id=1)


class HomeView(HHListView):
    model = Transaction
    queryset = Transaction.objects.order_by('-date')
    template_name = 'barkasse/home.html'

    def get_queryset(self):
        return super().get_queryset()[:5]


class TransactionList(HHListView):
    model = Transaction
    queryset = Transaction.objects.order_by('-date')


class TransactionCreate(HHCreateView):
    model = Transaction
    fields = ['shop','title','amount','account']
    reverse_url = 'barkasse:transactions'

    def get_form(self, *args, **kwargs):
        form = super(TransactionCreate, self).get_form(*args, **kwargs)
        form.fields['shop'].queryset = Shop.objects.filter(household=self.request.resolver_match.kwargs['hh'])
        form.fields['account'].queryset = Account.objects.filter(household=self.request.resolver_match.kwargs['hh'])
        return form


class TransactionUpdate(HHUpdateView):
    model = Transaction
    fields = ['shop','title','amount','account']
    reverse_url = 'barkasse:transactions'

    def get_form(self, *args, **kwargs):
        form = super(TransactionUpdate, self).get_form(*args, **kwargs)
        form.fields['shop'].queryset = Shop.objects.filter(household=self.request.resolver_match.kwargs['hh'])
        form.fields['account'].queryset = Account.objects.filter(household=self.request.resolver_match.kwargs['hh'])
        return form



class TransactionDelete(HHDeleteView):
    model = Transaction
    reverse_url = 'barkasse:transactions'


class ShopList(HHListView):
    model = Shop


class ShopCreate(HHCreateView):
    model = Shop
    fields = ['name']
    reverse_url = 'barkasse:shops'


class ShopUpdate(HHUpdateView):
    model = Shop
    fields = ['name']
    reverse_url = 'barkasse:shops'


class ShopDelete(HHDeleteView):
    model = Shop
    fields = ['name']
    reverse_url = 'barkasse:shops'


class AccountList(HHListView):
    model = Account


class AccountCreate(HHCreateView):
    model = Account
    fields = ['name', 'comment']
    reverse_url = ('barkasse:accounts')


class AccountUpdate(HHUpdateView):
    model = Account
    fields = ['name', 'comment']
    reverse_url = ('barkasse:accounts')


class AccountDelete(HHDeleteView):
    model = Account
    fields = ['name', 'comment']
    reverse_url=('barkasse:accounts')
import csv

from barkasse.models import Transaction, Shop, Account, Household, Member
from barkasse.household import HHListView, HHCreateView, HHUpdateView, HHDeleteView, HHMixin

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
from django.conf import settings
from django.shortcuts import redirect
from django.db.models.functions import TruncMonth
from django.db.models import Count

def export_csv_view(request, hh, year, month):
    # Create the HttpResponse object with the appropriate CSV header.

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, reverse_lazy('barkasse:home', args=[hh])))
    elif Member.objects.filter(household=hh, user=request.user):
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="export.csv"'},
        )

        transactions = Transaction.objects.filter(household=hh).filter(date__year=year,
                      date__month=month)

        writer = csv.writer(response)
        writer.writerow(['Date', 'Description', 'ContraAccount', 'Account', 'Amount'])

        for tr in transactions:
            if tr.title:
                text = tr.shop.name + ": " + tr.title
            else:
                text = tr.shop.name

            writer.writerow([tr.date.strftime("%Y-%m-%d"), text, tr.account.number, 4000, tr.amount])

        return response
    else:
        return redirect(reverse_lazy('barkasse:households'))


class ExportView(HHMixin, generic.TemplateView):
    template_name = 'barkasse/export.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hh'] = self.request.resolver_match.kwargs['hh']
        context['hh_name'] = Household.objects.get(id=self.request.resolver_match.kwargs['hh'])

        transactions = Transaction.objects.filter(household=self.request.resolver_match.kwargs['hh']).annotate(month=TruncMonth('date')).values('month').annotate(c=Count('id')).values('month', 'c')

        links = []

        for tr in transactions:
            link = {'url': reverse_lazy('barkasse:export_csv', args=[self.request.resolver_match.kwargs['hh'], tr['month'].strftime("%Y"), tr['month'].strftime("%m")]),
                    'count': tr['c'],
                    'month': tr['month'].strftime("%B"),
                    'year': tr['month'].strftime("%Y")}
            links.append(link)

        context['links'] = links

        return context


class HouseholdList(LoginRequiredMixin, generic.ListView):
    model = Household

    def get_queryset(self):
        return Household.objects.filter(member__user=self.request.user)



class HomeView(HHListView):
    model = Transaction
    queryset = Transaction.objects.order_by('-date')
    template_name = 'barkasse/home.html'

    def get_queryset(self):
        return super().get_queryset()[:5]


class TransactionList(HHListView):
    model = Transaction
    queryset = Transaction.objects.order_by('-date')
    paginate_by = 10


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
    fields = ['name', 'comment', 'number']
    reverse_url = ('barkasse:accounts')


class AccountUpdate(HHUpdateView):
    model = Account
    fields = ['name', 'comment', 'number']
    reverse_url = ('barkasse:accounts')


class AccountDelete(HHDeleteView):
    model = Account
    fields = ['name', 'comment', 'number']
    reverse_url=('barkasse:accounts')
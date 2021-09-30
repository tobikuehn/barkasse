from barkasse.models import Transaction, Shop, Account

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


class HomeView(LoginRequiredMixin, generic.ListView):
    model = Transaction
    queryset = Transaction.objects.order_by('-date')[:5]
    template_name = 'barkasse/home.html'


class TransactionList(LoginRequiredMixin, generic.ListView):
    model = Transaction
    queryset = Transaction.objects.order_by('-date')


class TransactionCreate(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = '__all__'
    success_url = reverse_lazy('barkasse:home')


class TransactionUpdate(LoginRequiredMixin, UpdateView):
    model = Transaction
    fields = '__all__'
    success_url = reverse_lazy('barkasse:home')


class TransactionDelete(LoginRequiredMixin, DeleteView):
    model = Transaction
    fields = '__all__'
    success_url = reverse_lazy('barkasse:home')


class ShopList(LoginRequiredMixin, generic.ListView):
    model = Shop


class ShopCreate(LoginRequiredMixin, CreateView):
    model = Shop
    fields = '__all__'
    success_url = reverse_lazy('barkasse:shops')


class ShopUpdate(LoginRequiredMixin, UpdateView):
    model = Shop
    fields = '__all__'
    success_url = reverse_lazy('barkasse:shops')


class ShopDelete(LoginRequiredMixin, DeleteView):
    model = Shop
    fields = '__all__'
    success_url = reverse_lazy('barkasse:shops')


class AccountList(LoginRequiredMixin, generic.ListView):
    model = Account


class AccountCreate(LoginRequiredMixin, CreateView):
    model = Account
    fields = '__all__'
    success_url = reverse_lazy('barkasse:accounts')


class AccountUpdate(LoginRequiredMixin, UpdateView):
    model = Account
    fields = '__all__'
    success_url = reverse_lazy('barkasse:accounts')


class AccountDelete(LoginRequiredMixin, DeleteView):
    model = Account
    fields = '__all__'
    success_url = reverse_lazy('barkasse:accounts')
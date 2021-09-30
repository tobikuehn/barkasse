from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name='barkasse'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('tr/', views.TransactionList.as_view(), name='transactions'),
    path('tr/create/', views.TransactionCreate.as_view(), name='transaction_create'),
    path('tr/<int:pk>/update/', views.TransactionUpdate.as_view(), name='transaction_update'),
    path('tr/<int:pk>/delete/', views.TransactionDelete.as_view(), name='transaction_delete'),
    path('shop/', views.ShopList.as_view(), name='shops'),
    path('shop/create/', views.ShopCreate.as_view(), name='shop_create'),
    path('shop/<int:pk>/update/', views.ShopUpdate.as_view(), name='shop_update'),
    path('shop/<int:pk>/delete/', views.ShopDelete.as_view(), name='shop_delete'),
    path('account/', views.AccountList.as_view(), name='accounts'),
    path('account/create/', views.AccountCreate.as_view(), name='account_create'),
    path('account/<int:pk>/update/', views.AccountUpdate.as_view(), name='account_update'),
    path('account/<int:pk>/delete/', views.AccountDelete.as_view(), name='account_delete'),
]

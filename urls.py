from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name='barkasse'
urlpatterns = [
    path('', views.HouseholdList.as_view(), name='households'),
    path('<int:hh>/', views.HomeView.as_view(), name='home'),
    path('<int:hh>/tr/', views.TransactionList.as_view(), name='transactions'),
    path('<int:hh>/tr/create/', views.TransactionCreate.as_view(), name='transaction_create'),
    path('<int:hh>/tr/<int:pk>/update/', views.TransactionUpdate.as_view(), name='transaction_update'),
    path('<int:hh>/tr/<int:pk>/delete/', views.TransactionDelete.as_view(), name='transaction_delete'),
    path('<int:hh>/shop/', views.ShopList.as_view(), name='shops'),
    path('<int:hh>/shop/create/', views.ShopCreate.as_view(), name='shop_create'),
    path('<int:hh>/shop/<int:pk>/update/', views.ShopUpdate.as_view(), name='shop_update'),
    path('<int:hh>/shop/<int:pk>/delete/', views.ShopDelete.as_view(), name='shop_delete'),
    path('<int:hh>/account/', views.AccountList.as_view(), name='accounts'),
    path('<int:hh>/account/create/', views.AccountCreate.as_view(), name='account_create'),
    path('<int:hh>/account/<int:pk>/update/', views.AccountUpdate.as_view(), name='account_update'),
    path('<int:hh>/account/<int:pk>/delete/', views.AccountDelete.as_view(), name='account_delete'),
    path('<int:hh>/export/', views.ExportView.as_view(), name='export'),
    path('<int:hh>/export/<int:year>/<int:month>', views.export_csv_view, name='export_csv'),
]

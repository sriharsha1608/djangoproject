from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('createpost', views.createpost, name="createpost"),
    path('nlrdetail', views.nlrdetail, name="nlrdetail"),
    path('inventory', views.inventory, name="inventory"),
    path('item', views.item, name="item"),
    path('branch', views.branch, name="branch"),
    path('transaction', views.transaction, name="transaction"),
]
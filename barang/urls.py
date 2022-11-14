from django.contrib import admin
from django.urls import path
from barang.views import *

urlpatterns = [
    path('list', barang_list, name='barang_list'),
    path('add', barang_add, name='barang_add'),
    path('update/<int:id>', barang_update, name='barang_update'),
    path('delete/<int:id>', barang_delete, name='barang_delete'),
]

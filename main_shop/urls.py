# main_shop/urls.py
from django.urls import path
from . import views

app_name = 'shop'  # Ось цей простір імен шукає ваш шаблон!

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
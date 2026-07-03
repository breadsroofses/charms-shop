# main_shop/urls.py
from django.urls import path
from . import views

app_name = 'shop'  # Ось цей простір імен шукає ваш шаблон!

urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    # 2. Потім головна сторінка:
    path('', views.product_list, name='product_list'),

    # 3. І ТІЛЬКИ В САМОМУ КІНЦІ — динамічний слаг категорій:
    # (у вас цей рядок може трохи відрізнятися, головне — його позиція внизу)
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),



]

app_name = 'main_shop' # Перевірте, чи є у вас цей namespace



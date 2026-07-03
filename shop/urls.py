# shop/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Підключаємо файл urls.py з додатка main_shop
    path('', include('main_shop.urls')),

    path('admin/', admin.site.urls),
    # Додаємо namespace сюди:
    path('', include('main_shop.urls', namespace='shop')),
]
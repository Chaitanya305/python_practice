"""
URL configuration for text_viewer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import viewer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewer.home, name='home'),
    path('home/', viewer.home, name='home'),
    path('about', viewer.about, name='about'),
    path('cart', viewer.cart, name='cart'),
    path('one', viewer.read_one, name='one' ),
]

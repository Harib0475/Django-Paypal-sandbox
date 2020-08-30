"""Django_Paypal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView

from Django_Paypal import viwes

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^paypal/', include('paypal.standard.ipn.urls')),
    path('payment_process/', viwes.payment_process, name='payment_process'),
    path('payment_done/$', TemplateView.as_view(template_name="payment_done.html"), name='payment_done'),
    path('payment_canceled/$', TemplateView.as_view(template_name="payment_canceled.html"), name='payment_canceled'),
]

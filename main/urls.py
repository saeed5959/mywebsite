"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from app import views
from azbankgateways.urls import az_bank_gateways_urls

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/signup', views.SignUpView.as_view(), name='signup'),
    path('accounts/panel', views.panel),
    path('accounts/panel/info', views.panel_info),
    path('accounts/panel/credit', views.panel_credit),
    path('accounts/panel/comment', views.panel_comment),
    path('cv', views.cv),
    path('blog', views.blog),
    path('bankgateways/', az_bank_gateways_urls()),
]

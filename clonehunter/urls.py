"""clonehunter URL Configuration

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
from  products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name ='home'),
    path('accounts/', include('accounts.urls')), # when we go to accounts urls we will be able to access to others sites
    # accounts.urls . here we tell to browser to go on folder accounnts and find urls.py where ww will put our urls
]

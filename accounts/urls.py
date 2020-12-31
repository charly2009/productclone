from django.conf.urls.static import static

from django.urls import path
from . import views
# allow as to grab everything from views


urlpatterns = [


    path('signup', views.signup, name='signup'), # accounts/signup
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),

]

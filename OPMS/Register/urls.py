from django.conf.urls import url
# from apps import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from Register import views

urlpatterns = [
    url(r'^$',views.index),
    #url(r'^register$',views.register),
    #url(r'^success$',views.success),
    url(r'^login$',auth_views.LoginView.as_view(template_name = 'login.html'),name = 'login'),
    url(r'^logout$',auth_views.LogoutView.as_view(),name = 'logout'),
    url(r'^signin$',views.SignUp.as_view(),name = 'signup'),
    url(r'^homePage$',views.homePage,name = 'homePage'),

    ]

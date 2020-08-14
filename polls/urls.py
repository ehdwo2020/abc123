from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('areas/<str:area>/', views.areas),
    path('polls/<int:poll_id>/', views.polls)]
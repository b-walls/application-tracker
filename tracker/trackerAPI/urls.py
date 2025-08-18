from django.urls import path
from . import views

urlpatterns = [
    path('api/applications', views.ApplicationView.as_view()),
    path('', views.home_view, name='home')
]
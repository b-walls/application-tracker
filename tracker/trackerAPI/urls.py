from django.urls import path
from . import views

urlpatterns = [
    path('api/applications', views.ApplicationView.as_view()),
    path('api/applications/<int:pk>', views.SingleApplicationView.as_view(), name="single_application"),
    path('api/company/create', views.CompanyCreateView.as_view()),
    path('api/posting/create', views.PostingCreateView.as_view()),
    path('', views.home_view, name='home'),
]
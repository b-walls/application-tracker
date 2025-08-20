from django.urls import path
from . import views

urlpatterns = [
    # renders
    path('', views.home_view, name='home'),
    path('applications/<int:pk>', views.single_app_view, name="single_application"),
    path('new', views.create_app_view, name="new"),

    # api endpoints
    path('api/applications', views.ApplicationView.as_view()),
    path('api/applications/<int:pk>', views.SingleApplicationView.as_view()),
    path('api/company', views.CompanyCreateView.as_view()),
    path('api/posting', views.PostingCreateView.as_view()),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.Contact_View, name='contact'),
    path('tours/success', views.Contact_Success_View, name='contact-success'),
]

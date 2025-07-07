from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.Contact_View, name='contact'),
    path('tours/success', views.Contact_Success_View, name='contact-success'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]

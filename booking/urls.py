from django.urls import path
from booking import views

urlpatterns = [
    path('', views.view_home, name='home'),
    path('services/', views.view_services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.view_about, name='about'),   
    path('blog/', views.view_blog, name='blog'),
    path('add_booking/', views.add_booking, name='add_booking'),
    path('view_booking/', views.view_booking, name='view_booking'),
    path('edit/<booking_id>', views.edit_booking, name='edit_booking'),
    path('delete/<booking_id>', views.delete_booking, name='delete_booking'),
]
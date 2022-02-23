from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/add', views.create_restaurant),
    path('restaurants/new', views.add_restaurant),
    path('landing', views.landing_page),
    path('restaurants', views.about_us),
    path('restaurants/<int:rest_id>', views.restaurant_details),
    
]

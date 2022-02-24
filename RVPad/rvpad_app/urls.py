from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/new', views.add_restaurant),
    path('restaurants/add', views.create_restaurant),
    path('landing', views.landing_page),
    path('about_us', views.about_us),
    path('restaurants', views.restaurants),
    path('restaurants/<int:rest_id>', views.restaurant_details),
    path('reviews/add/<int:rest_id>', views.add_review),
    
]

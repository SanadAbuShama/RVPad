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
    path('users/<int:user_id>', views.user_profile),
    path('restaurants/delete/<int:rest_id>', views.restaurant_delete),
    path('reviews/delete/<int:rev_id>/<int:rest_id>', views.review_delete),
]


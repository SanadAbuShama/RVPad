from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing),
    path('login_register', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('profile', views.profile),
    path('email', views.email),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

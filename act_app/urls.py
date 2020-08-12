from django.urls import path
from . import views

urlpatterns = [
    path('user_data/', views.get_data),
]

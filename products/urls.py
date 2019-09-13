from django.urls import path
from . import views

# path('') - represents the root of that path
urlpatterns = [
    path('', views.index),
    path('new/', views.new)
]
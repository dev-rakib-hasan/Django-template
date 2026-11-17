from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.create_blog, name='create_blog')
]

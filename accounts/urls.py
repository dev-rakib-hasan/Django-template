from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.create_blog, name='create_blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
]

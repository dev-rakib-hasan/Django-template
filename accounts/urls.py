
from django.urls import path
from . import views

urlpatterns = [
    # Register Login URLs
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    # Blog API URLs
    path('blog_list_create/', views.blog_list_create, name='blog_list_create'),
    path('blog_detail/<int:pk>/', views.blog_detail, name='blog_detail'),
    #Blog Like or Comment URLs
    path('blog_like/<int:pk>/', views.blog_like, name='blog_like'),
    path('blog_comment/<int:pk>/', views.blog_comment, name='blog_comment'),


    # HTML Template URLs
    path('blogs/', views.blog_list, name='blog_list'),
    path('blog/create/', views.blog_create_page, name='blog_create'),

    path('blog/<int:pk>/',
         views.blog_list_id,
         name='blog_detail'),

    path('blog/update/<int:pk>/',
         views.blog_update_page,
         name='blog_update'),

    path('blog/delete/<int:pk>/',
         views.blog_delete_page,
         name='blog_delete'),
]

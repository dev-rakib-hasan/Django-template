
from django.urls import path
from . import views

urlpatterns = [

    # Swagger / API URLs
    path('blog/', views.create_blog, name='create_blog'),
    path('api/blog/<int:pk>/', views.blog_detail, name='api_blog_detail'),

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

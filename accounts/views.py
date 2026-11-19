from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import BlogSerializer
from rest_framework import status
from .models import Blog

# Create your views here.

@api_view(['GET','POST'])
def create_blog(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(
            serializer.data
            )
    
    serializer = BlogSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED
        )
    
@api_view(['GET', 'PUT','PATCH','DELETE'])
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
  # GET API  
    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    elif request.method == ['PUT','PATCH']:
        if request.method == 'PATCH':
            serializer = BlogSerializer(
                blog,
                data=request.data,
                partial=True
                )
        
        else: 
            serializer = BlogSerializer(
                blog,
                data=request.data,
                
            )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        blog.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
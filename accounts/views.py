from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import(
    extend_schema,
    OpenApiResponse,
    OpenApiRequest,
    OpenApiParameter,
)
from .models import(
    Blog
)
from .serializers import(
    BlogSerializer
)




# Show All Blogs
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'accounts/blog_list.html', {'blogs': blogs})


# Create Blog
def blog_create_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Blog.objects.create(
            title=title,
            description=description
        )

        return redirect('blog_list')

    return render(request, 'accounts/blog_create.html')


# Show blog
def blog_list_id(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    return render(request, 'accounts/blog_detail.html', {'blog': blog})


# Update Blog
def blog_update_page(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.description = request.POST.get('description')
        blog.save()

        return redirect('blog_list')
    return render(request, 'accounts/blog_detail.html', {'blog': blog})
    


# Delete Blog
def blog_delete_page(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        blog.delete()

    return redirect('blog_list')




#===============
# DRF API VIEWS
#===============

@extend_schema(
    tags=['Blog'],
    summary='create Blog',
    description=('Retrieve all blog or New blog'),
    request=BlogSerializer,
    responses={
        200:BlogSerializer(many=True),
        201:OpenApiResponse(description='Added Successfully,.'),
        400:OpenApiResponse(description='Validation Error')
    },
)

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
    
@extend_schema(
    tags=['Blog'],
    summary='Retrieve update or delete blog',
    description='Retrieve Update or delete using ID.',
    request=BlogSerializer,
    responses={
        200:BlogSerializer,
        204:OpenApiResponse(description='Blog Deleted Successfully'),
        400:OpenApiResponse(description='Validation Error'),
        404:OpenApiResponse(description='Blog Not Found')
    },
)
    
@api_view(['GET', 'PUT','PATCH','DELETE'])
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
  # GET API  
    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    elif request.method in ['PUT','PATCH']:
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
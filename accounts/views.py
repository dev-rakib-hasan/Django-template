from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializer
from rest_framework import status
from .models import Blog

# Create your views here.

@api_view(['POST'])
def create_blog(request):
    serializer = BlogSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return Response({'message':'Blog Create Successfully', 'data':serializer.data}, status=status.HTTP_201_CREATED)
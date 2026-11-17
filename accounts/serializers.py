from rest_framework import serializers
from . models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meat:
        model = Blog
        fields = [
            'id',
            'title'
            'description',
            'created_at',
            'updated_at'
            ]
        
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]
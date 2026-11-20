from rest_framework import serializers
from . models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'id', 
            'slug',
            'created_at',
            'updated_at',
        ]

from django.db import models
import uuid

# Create your models here.
 
class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=155)
    descrition = models.TextField
    created_at = models.BooleanField(auto_now_add=True)
    updated_at = models.BooleanField(auto_now=True)
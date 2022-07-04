from rest_framework import serializers
from .models import Post
from django import forms

#same as forms, but from somewhere else? conversion of post model to json one()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post 
        fields=(
            'title','description'
        )
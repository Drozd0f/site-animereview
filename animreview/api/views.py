from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from reviews.models import Posts
from .serializers import PostsSerializer


class PostShowView(generics.ListAPIView):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()

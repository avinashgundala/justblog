from rest_framework.generics import (
                                     ListAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     CreateAPIView,
                                                     )
from blog.models import Post
from .serializers import PostSerializer,PostCreateSerializer

class PostListAPIView(ListAPIView):
     queryset   = Post.objects.all()
     serializer_class = PostSerializer

class PostDetailAPIView(RetrieveAPIView):
     queryset   = Post.objects.all()
     serializer_class = PostSerializer

class PostUpdateAPIView(UpdateAPIView):
     queryset   = Post.objects.all()
     serializer_class = PostSerializer

class PostDeleteAPIView(DestroyAPIView ):
     queryset   = Post.objects.all()
     serializer_class = PostSerializer

class PostCreateAPIView(CreateAPIView ):
     queryset   = Post.objects.all()
     serializer_class = PostCreateSerializer

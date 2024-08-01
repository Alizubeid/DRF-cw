from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.models import Category, Post
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import PostSerializer, CategorySerializer


class PostListView(APIView):

    def get(self, request, format=None):
        posts_list_obj = Post.objects.all()
        serializer = PostSerializer(posts_list_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer_obj = PostSerializer(data=request.data)
        serializer_obj.is_valid(raise_exception=True)
        serializer_obj.save()
        return Response(serializer_obj.data, status=status.HTTP_201_CREATED)


class CategoryListView(APIView):

    def get(self, request, format=None):
        categories_list_obj = Category.objects.all()
        ser = CategorySerializer(categories_list_obj, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class PostDetailView(APIView):

    def put(self, request, pk):
        post_obj = get_object_or_404(Post, pk=pk)
        # serializer = PostSerializer(post_obj, data=request.data)
        serializer = PostSerializer(post_obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        post_obj = get_object_or_404(Post, pk=pk)
        post_obj.delete()
        return Response({"detail": "obj was deleted!"})

    def get(self, request, pk):
        post_obj = Post.objects.get(pk=pk)
        serializer = PostSerializer(post_obj)
        return Response(serializer.data)


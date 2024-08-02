from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from blog.models import Category, Post, Comment
from .serializers import PostSerializer, CategorySerializer, CommentListSerializer, ReplySerializer, CommentSerializer


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


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentListSerializer


class CommentViewSet(viewsets.ViewSet):
    @action(methods=['post'], detail=False)
    def create_reply(self, request):
        serializer = ReplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_object(self, pk):
        return get_object_or_404(Comment, pk=pk)

    def list(self, request):
        comments = Comment.objects.all()
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        comment = self.get_object(pk)
        serializer = CommentListSerializer(comment)
        return Response(serializer.data)

    def update(self, request, pk=None):
        serializer = CommentSerializer(self.get_object(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        instances = self.get_object(pk)
        serializer = CommentSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(instance=instances, validated_data=serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response({"detail": "Comment has been deleted"}, status=status.HTTP_204_NO_CONTENT)

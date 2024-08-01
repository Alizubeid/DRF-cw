from django.urls import path
from .views import PostListView, CategoryListView, PostDetailView

urlpatterns = [
    path("post/", PostListView.as_view(), name="post-list"),
    path("category/", CategoryListView.as_view(), name="category-list"),
    path("post/detail/<pk>/", PostDetailView.as_view(), name="post-detail"),
    
]

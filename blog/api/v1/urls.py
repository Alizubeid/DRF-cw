from django.urls import path
from .views import PostListView, CategoryListView, PostDetailView, CommentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comments')
urlpatterns = router.urls

urlpatterns += [
    path("post/", PostListView.as_view(), name="post-list"),
    path("category/", CategoryListView.as_view(), name="category-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    
]

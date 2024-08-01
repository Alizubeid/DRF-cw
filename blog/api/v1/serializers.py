from rest_framework.serializers import ModelSerializer, SlugRelatedField
from blog.models import Post, Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerializer(ModelSerializer):
    # categories = SlugRelatedField(slug_field="name",read_only=True)
    # categories = CategorySerializer(many=True)


    # show title pk categories => {'categories': [{'name': 'computer'}], 'title': 'intel', 'description': 'null'}
    # normal => {'title': 'intel', 'description': 'null', 'categories': [<Category: computer>]}


    class Meta:
        model = Post
        fields = "__all__"


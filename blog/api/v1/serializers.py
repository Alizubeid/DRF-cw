from rest_framework.serializers import ModelSerializer, SlugRelatedField
from blog.models import Post, Category, Comment


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


class CommentListSerializer(ModelSerializer):
    # def validate_replied_comment(self, attrs):
    #     pass
    # if self.replied_comment:
    #     if self.post and self.post != self.replied_comment.post:
    #         raise ValueError("The 'post' of a reply can't be different from the 'post' of the replied comment")
    #     else:
    #         self.post = self.replied_comment.post
    # super(Comment, self).save(*args, **kwargs)

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['replied_comment']


class ReplySerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['post']

    def create(self, validated_data):
        replied_comment = validated_data.get('replied_comment')
        return Comment.objects.create(**validated_data, post=replied_comment.post)

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=64)
    description = models.TextField()
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True)
    replied_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if self.replied_comment:
    #         if self.post and self.post != self.replied_comment.post:
    #             raise ValueError("The 'post' of a reply can't be different from the 'post' of the replied comment")
    #         else:
    #             self.post = self.replied_comment.post
    #     super(Comment, self).save(*args, **kwargs)

# class Reply(models.Model):
#     reply = models.TextField()
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

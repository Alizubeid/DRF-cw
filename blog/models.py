from django.db import models


class Post(models.Model):
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
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    parrent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.post and self.parrent:
            self.post = self.parrent.post
        return super(Comment, self).save(self, *args, **kwargs)


# class Reply(models.Model):
#     reply = models.TextField()
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

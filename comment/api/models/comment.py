from django.db import models
from django.contrib.auth.models import User
from post_data.api.models.post import Post
from django.utils import timezone


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_date = models.DateTimeField(editable=False)

    class Meta:
        ordering = ('created_date',)

    def __str__(self):
        return self.post.title + " " + self.user.username

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()

        self.modified_date = timezone.now()
        return super(Comment, self).save(*args, **kwargs)

    def children(self):
        return Comment.objects.filter(parent= self)

    @property
    def any_children(self):
        return Comment.objects.filter(parent = self).exists()

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField()
    draft = models.BooleanField(default=False)  # taslaklara kaydetme
    created_date = models.DateTimeField(editable=False)
    modified_date = models.DateTimeField()
    slug = models.SlugField(unique=True, max_length=150, editable=False)

    def get_slug(self):
        slug = slugify(self.title.replace("ı","i"))
        unique = slug
        number = 1
        while

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()

        self.modified_date = timezone.now()

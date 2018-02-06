from django.db import models

# Create your models here.
class Articles (models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    author = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str___(self):
        return self.title

    def is_updated(self):
        return created_at != updated_at

from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

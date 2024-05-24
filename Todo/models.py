from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='todo',default='default.jpg')
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
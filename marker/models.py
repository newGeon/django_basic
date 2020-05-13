from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Photo(models.Model):
    file_name = models.CharField(max_length=200)
    file_path = models.CharField(max_length=400)

class Position(models.Model):
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)
    coordinate_x = models.FloatField()
    coordinate_y = models.FloatField()

class User(models.Model):
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    user_status = models.CharField(max_length=10)
    user_roles = models.CharField(max_length=10)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "user_info"

from django.db import models
from users.models import User
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=50, null=True)
    scientific_name = models.CharField(max_length=50, unique=True)
    origin = models.CharField(max_length=50, null=True)
    image_url = models.TextField(max_length=600)
    about = models.TextField(max_length=600)
    last_modf = models.DateTimeField(default=timezone.now)
    contributor = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.scientific_name
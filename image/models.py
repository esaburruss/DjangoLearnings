from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ImageUpload(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    owner = models.ForeignKey(User)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)
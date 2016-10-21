from django.db import models

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=30)
    pos = models.IntegerField()
    isVisible = models.IntegerField()
    class Meta:
        ordering = ['pos']
	
	
class Page(models.Model):
    name = models.CharField(max_length=30)
    pos = models.IntegerField()
    content = models.CharField(max_length=10000)
    section = models.ForeignKey(Section)
    isVisible = models.IntegerField()
    class Meta:
        ordering = ['pos']
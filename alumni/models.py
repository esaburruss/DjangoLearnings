from django.db import models

class Brother(models.Model):
    isApproved = models.IntegerField()
    isAlumni = models.IntegerField()
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    nickName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    badge = models.IntegerField()
    gradYear = models.IntegerField()
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=50)
    zip = models.IntegerField()
    streetAddress = models.CharField(max_length=100)
    pledgeClass = models.CharField(max_length=50)
    occupation = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    linkedIn = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

class Exec(models.Model):
    title = models.CharField(max_length=100)
    rank = models.IntegerField()
    brothers = models.ManyToManyField(Brother)
    class Meta:
        ordering = ['rank']
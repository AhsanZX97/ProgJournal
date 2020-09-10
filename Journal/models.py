from django.db import models

# Create your models here.
class resource(models.Model):
    name = models.CharField(max_length=64, blank=False)
    link = models.URLField()
    image = models.FileField(null=True,blank=True)
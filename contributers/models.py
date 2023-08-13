from django.db import models


class contributersDetails(models.Model):
    c_name = models.TextField(max_length=50)
    c_image=models.ImageField(upload_to='contributersImage')
    c_bio = models.TextField(max_length=200)

# Create your models here.

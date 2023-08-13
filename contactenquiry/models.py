from django.db import models


class contactenquiry(models.Model):
    contact_name = models.CharField(max_length=50,blank=False,null=False)
    contact_email = models.CharField(max_length=50,blank=False,null=False)
    contact_desc = models.TextField(blank=False)
# Create your models here.

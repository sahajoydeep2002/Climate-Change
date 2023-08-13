from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class blogPost(models.Model):
    author_name= models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=False,null=False)
    content = models.TextField(blank=False)
    date_posted = models.DateTimeField(default=timezone.localtime)

    def _str_(self):
        return self.title 
    def get_absolute_url(self):
        return reverse("blog-post", kwargs={"pk": self.pk})
    



# Create your models here.

from django.db import models


class quesModel(models.Model):
    ques = models.CharField(max_length=200,null=True)
    opt1 = models.CharField(max_length=200,null=True)
    opt2 = models.CharField(max_length=200,null=True)
    opt3 = models.CharField(max_length=200,null=True)
    opt4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    level = models.CharField(max_length=200,null=True)


    def __str__(self):
        return self.ques

# Create your models here.

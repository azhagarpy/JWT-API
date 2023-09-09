from django.db import models

# Create your models here.


class CODERS(models.Model):
    UserName=models.CharField(max_length=25,blank=False,null=False)
    PassWord=models.CharField(max_length=25,blank=False,null=False)
    CreatedAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.UserName
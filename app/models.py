from django.db import models

class Urls(models.Model):
    #the short url is a 7 chars string so there is no need for more space
    short_url = models.CharField(max_length=10,unique=True,null=False,blank=False)
    #used text field instead of char field to not specify the length of the original url,
    #because it could be long
    origin_url = models.TextField(null=False,blank=False,unique=False)
    counter = models.PositiveBigIntegerField(null=False,default=0,blank=False,unique=False)

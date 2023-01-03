from django.db import models

class Urls(models.Model):
    short_url = models.CharField(max_length=255,unique=True,null=False,blank=False)
    #used text field instead of char field to not specify the length of the original url,
    #because it could be long
    origin_url = models.TextField(null=False,blank=False,unique=False)
    # should be big enought to store all the clicks, could be a lot of them 
    # what is there is still not enought room? maybe switch? msybe start smaller to not take up unnesecery space
    #maybe django takes care of it?
    counter = models.PositiveBigIntegerField(null=False,default=0,blank=False,unique=False)

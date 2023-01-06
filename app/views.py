from operator import mod
from pyexpat import model
from tkinter.messagebox import showerror
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from app import models
from django.shortcuts import redirect
import secrets
import string
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseNotFound



class UrlView(APIView):
    def get(self,request,*args,**kwargs):
        return HttpResponse("Hellooo!!")

    def post(self,request,*args,**kwargs):
        original_url = request.data['url']
        try:
            obj = models.Urls.objects.get(origin_url = original_url)
            short_url = obj.short_url
        except:
            short_url = self.generate_short_url()
            models.Urls(origin_url = original_url,short_url = short_url).save()
        return Response('http://localhost:8000/'+short_url)

    def generate_short_url(self):
        # there are 36^7 options for a short url, the possibillity for the 
        # generator to generate a url that is already used is small but increasing as the urls in the data base increase.
        # Over time, if used a lot, the unique urls could run out. 
        # In that case, we should check the number of urls in data base an make some cut off to increase N.
        # another option is to delete unused urls.
        N = 7
        res = ''.join(secrets.choice(string.ascii_lowercase + string.digits)
                    for i in range(N))
        return res

class CatchView(APIView):
    def get(self,request,*args,**kwargs):
        short_url = kwargs['p']
        try:
            obj = models.Urls.objects.get(short_url = short_url)
            obj.counter+=1
            obj.save()
            origin_url = obj.origin_url
            response = redirect(origin_url)
            return response
        except:
            return HttpResponseNotFound("sorry, this url does not exist")

    
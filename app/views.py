from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from app import models
from django.shortcuts import redirect
#does it count as dependenses?
import secrets
import string
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator




class HelloWorldView(APIView):

    def get(self,request,*args,**kwargs):
        print("77777777777")
        return HttpResponse("Hello world!!!!")

    def post(self,request,*args,**kwargs):
        print("777777777778888")
        original_url = request.data['url']
        #generate short url
        short_url = self.generate_short_url()
        models.Urls(origin_url = original_url,short_url = short_url).save()
        return Response('http://localhost:8000/'+short_url)

    def generate_short_url(self):
        # initializing size of string
        #explain the number choise
        N = 7
        
        # using secrets.choice()
        # generating random strings
        res = ''.join(secrets.choice(string.ascii_letters + string.digits)
                    for i in range(N))
        return res


class CatchView(APIView):
    def get(self,request,*args,**kwargs):
        print("6666666",kwargs['p'])
        short_url = kwargs['p']
        #check if this short url exists in database
        #tru catch
        obj = models.Urls.objects.get(short_url = short_url)
        obj.counter+=1
        obj.save()
        origin_url = obj.origin_url
        print(origin_url)
        response = redirect(origin_url)
        return response

    
from django.shortcuts import render
from rest_framework.decorators import api_view
import json as simplejson
from django.http import HttpResponse,JsonResponse
from blog.models import Post 
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.

@api_view(['GET','POST'])
def first(request):
	
	postData = Post.objects.filter(id=request.POST.get("id"))

	#postData = Post.objects.all()
	if(len(postData)>=1):
		data = list(postData.values('title'))
		data =JsonResponse({'data':data})
	else:
		data = JsonResponse({'statusCode':1,'status':'No blog found',
			'len':len(postData),'id':request.COOKIES})
	return data
	#return True

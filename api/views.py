from django.shortcuts import render
from rest_framework.decorators import api_view
import json as simplejson
from django.http import HttpResponse,JsonResponse
from blog.models import Post 
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.
import json
@api_view(['GET','POST'])
def first(request):
	#result = json.loads(request.body)
	body = json.loads(request.body)
	return JsonResponse({'request_get':request.GET,
		'request_post':request.POST,'request_body':body})
	postData = Post.objects.filter(id=2)

	#postData = Post.objects.all()
	if(len(postData)>=1):
		data = list(postData.values('title'))
		data =JsonResponse({'data':data})
	else:
		data = JsonResponse({'statusCode':1,'status':'No blog found',
			'len':len(postData),'id':request.data})
	return data
	#return True

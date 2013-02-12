from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponsePermanentRedirect
import random
import string
from url.models import Data
from django import shortcuts
from django.views.decorators.csrf import csrf_exempt

def index(request):
	return render_to_response('index2.html')

@csrf_exempt
def redirect(request):
	org = request.POST['content']
	p=Data.objects.filter(actualurl =org)
	if p:
		tup = {'url':p[0].tinyurl}
		return shortcuts.render_to_response('index4.html',tup)


	else:
		list=[]
		for i in range(len(org)):
			if i%10==0:
				list.append(org[i])

		word=''.join(list)+random.choice(string.ascii_letters)
		a='http://127.0.0.1:8000/'+word	
		s=Data(actualurl=org, tinyurl=a,randomcode=word)
		s.save()
		tup = {}
		tup['url']=a
		return shortcuts.render_to_response('index4.html', tup)
		

def link(request,path):
	ref=request.path
	l=Data.objects.filter(randomcode=path)
	if l:
		tup= {'url':l[0].actualurl}
		return shortcuts.render_to_response('index6.html', tup)	




	

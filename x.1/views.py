from django.http import HttpRequest
from django.shortcuts import render
#from django.http import HttpResponse
# from django.template.loader import templates

def index(request):
	return render(request,'index.html')


def about(request):
	return render(request,'about.html')
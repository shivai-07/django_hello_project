from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index(request):
    return HttpResponse('''
        <h1>Hello Everyone...!</h1>
        <h4> Welcome to django Web Application....</h4>
    ''')

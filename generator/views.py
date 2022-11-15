from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random
import string

#import generator


def home(request):
    return render(request,'generator/home.html')
 #   return HttpResponse('Hello!!!Welcome to SportsMania')
def password(request):
    characters = list(string.ascii_lowercase)
    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('specials'):
        characters.extend(list(string.punctuation))
    if request.GET.get('numbers'):
        characters.extend(list(string.digits))
    length=int(request.GET.get('length'))
    thepassword = ''
    for i in range(length):

        thepassword+=random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})

def siteinfo(request):
    return render(request, 'generator/siteinfo.html')

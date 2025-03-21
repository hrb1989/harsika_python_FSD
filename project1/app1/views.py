from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        'test':'enable',
        'var1':'44'
    }
    return render(request, 'index.html', context)

def simple_page(request):
    return HttpResponse("<h1>This is a Simple Test Page</h1>")

# HTTP Response Codes
'''
200 - ok
300 - redirect
400 - data unavailable
500 - server issue
'''

def day2(request):
    context = {
        'var1':'11',
        'var2':'22',
        'var3':'33',
        'var4':'44'
    }
    return render(request, 'day2.html', context)
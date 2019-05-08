from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
#
def info(request):
    return render(request, 'info.html')


def addhosts(request):
    return render(request, 'addhosts.html')

def addmodules(request):
    return render(request, 'addmodules.html')

def tasks(request):
    return render(request, 'tasks.html')


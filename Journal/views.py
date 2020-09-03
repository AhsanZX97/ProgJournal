from django.http import HttpResponseRedirect
from django.shortcuts import render
from Journal.models import resource

# Create your views here.
def resources(request):
    all_todo_items = resource.objects.all()
    return render(request, 'resource.html',
    {'all_items':all_todo_items})

def addPage(request):
    return render(request, 'add.html')

def addResource(request):
    n = request.POST['name']
    l = request.POST['link']
    new_item = resource(name = n, link = l)
    new_item.save()
    return HttpResponseRedirect('/')

def delResource(request, i):
    res = resource.objects.get(id= i)
    res.delete()
    return HttpResponseRedirect('/')
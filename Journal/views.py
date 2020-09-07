from django.http import HttpResponseRedirect
from django.shortcuts import render
from Journal.models import resource

# Create your views here.
def resources(request):
    all_todo_items = resource.objects.all()
    return render(request, 'resource.html',
    {'all_items':all_todo_items})

def addPage(request,i = 0):
    if i > 0:
        res = resource.objects.get(id=i)
        return render(request, 'add.html',{'res':res})
    else:
        return render(request, 'add.html',{'res':False})

def editResource(request,i = 0):
    print("FIRST LINE")
    n = request.POST['editname']
    l = request.POST['editlink']
    item = resource.objects.get(id=i)
    print("RESOURCE IS:  " + str(l))
    item.name = n
    item.link = l
    item.save()
    return HttpResponseRedirect('/')

def addResource(request,i = 0):
    if i > 0:
        print("FIRST LINE")
        n = request.POST['editname']
        l = request.POST['editlink']
        item = resource.objects.get(id=i)
        print("RESOURCE IS:  " + str(l))
        item.name = n
        item.link = l
        item.save()
    else:
        n = request.POST['name']
        l = request.POST['link']
        new_item = resource(name = n, link = l)
        new_item.save()
    return HttpResponseRedirect('/')

def delResource(request, i):
    res = resource.objects.get(id= i)
    res.delete()
    return HttpResponseRedirect('/')
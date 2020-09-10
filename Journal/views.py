from django.core.files.storage import FileSystemStorage
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

def addResource(request,i = 0):
    if i > 0:
        n = request.POST['editname']
        l = request.POST['editlink']
        f = request.FILES['editfile']
        fs = FileSystemStorage()
        fs.save(f.name, f)
        item = resource.objects.get(id=i)
        item.name = n
        item.link = l
        item.image = f
        item.save()
    else:
        n = request.POST['name']
        l = request.POST['link']
        fs = FileSystemStorage()
        f = None
        try:
            f = request.FILES['file']
            fs.save(f.name, f)
        except:
            pass
        new_item = resource(name = n, link = l,image= f)
        new_item.save()
    return HttpResponseRedirect('/')

def delResource(request, i):
    res = resource.objects.get(id= i)
    res.delete()
    return HttpResponseRedirect('/')
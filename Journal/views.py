from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def resources(request):
    return render(request, 'resource.html')

def addPage(request):
    return render(request, 'add.html')

def addResource(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('')
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from todo2app.forms import Taskform
from todo2app.models import Task
def home(request):
    objs = Task.objects.all()
    if request.method=="POST":
        tas=request.POST.get("task")
        pri=request.POST.get("priority")
        dat = request.POST.get("date")
        obj=Task(task=tas,priority=pri,date=dat)
        obj.save()
        print(obj)
        print(objs,type(objs))
    return render(request,"home.html",{"key2":objs})
def details(request,id):
    obj=Task.objects.get(id=id)
    return render(request,"details.html",{"key2":obj})
def delete(request,taskid):
    obj1 = Task.objects.get(id=taskid)
    if request.method=="POST":
        obj1.delete()
        print("deleted")
        return redirect("/")
    return render(request,"delete.html")
def update(request,id):
    obj1=Task.objects.get(id=id)
    formobj1=Taskform(request.POST or None,instance=obj1)
    if formobj1.is_valid():
        formobj1.save()
        return redirect("/")
    return render(request,"update.html",{"key1":obj1,"key2":formobj1})
class Cbvlist(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name ='key2'
class Cbvdetails(DetailView):
    model=Task
    template_name = 'details.html'
    context_object_name ='key2'
class Cbvupdate(UpdateView):
    model=Task
    template_name='update2.html'
    context_object_name='key2'
    fields=('task','priority','date')
    def get_success_url(self):
        return reverse_lazy("Cbvdetails",kwargs={'pk':self.object.id})
class Cbvdelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url=reverse_lazy('Cbvlist')


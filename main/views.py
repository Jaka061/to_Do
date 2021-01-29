from django.shortcuts import render,HttpResponse
from .models import ToDo

def todo(request):
    todo_list = ToDo.objects.all()
    return render(request,"todo.html", {"todo_list" : todo_list})


def test(request):
    return render(request,"index.html")

def test2(request):
    return render(request,"test2.html")

def test3(request):
    return render(request,"test3.html")


# def third(request):
#     return HttpResponse("This is page test3")

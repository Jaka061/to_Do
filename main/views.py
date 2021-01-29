from django.shortcuts import render,HttpResponse
from .models import ToDo

def todo(request):
    return render(request,"todo.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request,"index.html", {"todo_list" : todo_list})

def test2(request):
    return render(request,"test2.html")

def test3(request):
    return render(request,"test3.html")


# def third(request):
#     return HttpResponse("This is page test3")

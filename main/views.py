from django.shortcuts import render,HttpResponse

def todo(request):
    return render(request,"todo.html")

def second(request):
    return HttpResponse(" Second pade Test2")

def third(request):
    return HttpResponse("This is page test3")

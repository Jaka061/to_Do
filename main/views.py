from django.shortcuts import render,HttpResponse

def homepage(request):
    return HttpResponse("Hello")

def test(request):
    return render(request,"index.html")
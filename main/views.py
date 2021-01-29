from django.shortcuts import render,HttpResponse

def todo(request):
    return render(request,"todo.html")


def test(request):
    return render(request,"index.html")

def test2(request):
    return render(request,"test2.html")

def test3(request):
    return render(request,"test3.html")


# def third(request):
#     return HttpResponse("This is page test3")

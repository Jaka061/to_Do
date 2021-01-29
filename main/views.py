from django.shortcuts import render,HttpResponse,redirect
from .models import ToDo ,Book

def todo1(request):
    todo_list = ToDo.objects.all()
    return render(request,"todo.html",{"todo_list" : todo_list})

# def test(request):
#     todo_list = ToDo.objects.all()
#     return render(request,"index.html", {"todo_list" : todo_list})

# # def book(request):
#     book_list = Book.objects.all()
#     return render(request,"book.html", {"book_list ": book_list})


def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(todo1)

from django.shortcuts import render,redirect
from . forms import TodoForm
from . models import Todo
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    todos = Todo.objects.all().order_by('-id')

    paginator = Paginator(todos, 3)  # Show 10 items per page

    page_number = request.GET.get('page')
    item_todo = paginator.get_page(page_number)

    if request.method == 'POST':
        form = TodoForm(request.POST,request.FILES,)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'index.html',{'todos':todos,'item_todo':item_todo})

def update(request,id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST,request.FILES, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm(instance=todo)
        return render(request, 'update.html',{'form':form})
def delete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')

def view(request,id):
    todo = Todo.objects.get(id=id)
    return render(request, 'view.html',{'todo':todo})

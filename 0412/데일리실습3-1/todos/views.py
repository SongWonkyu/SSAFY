from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):
    todos = Todo.objects.all()
    if not todos:
        message = '작성된 글이 없습니다.'
    else:
        message = None
    context={
        'todos':todos,
        'message': message,

    }
    return render(request, 'todos/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            if form.cleaned_data['completed']:
                todo.completed = True
            else:
                todo.completed = False
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context={
        'form':form
    }
    return render(request, 'todos/create.html', context)


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user == todo.author:
        todo.delete()
        return redirect('todos:index')

def toggle(request, pk):
    todo = get_object_or_404(Todo,pk=pk)
    if request.user == todo.author:
        todo.completed = not todo.completed
        todo.save()
    return redirect('todos:index')
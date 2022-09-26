from django.shortcuts import render
from todolist.models import Task
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from todolist.forms import TaskForm
from django.contrib.auth.decorators import login_required


todo_list_data = Task.objects.all().values()

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todo_list(request):
    context = {
        'todo_list': todo_list_data,  # data untuk HTML
        'nama': request.user.username,
    }
    return render(request, 'todolist.html', context)

def show_json(request):
    return HttpResponse(serializers.serialize("json", todo_list_data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    context = {
        'todo_list': todo_list_data,  # data untuk HTML
        'nama': request.user.username,
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todo_list')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def show_logout_page(request):
    context = {
        'todo_list': todo_list_data,  # data untuk HTML
        'nama': request.user.username,
    }
    return render(request, 'logout_page.html', context)

@login_required
def create_task(request):
    if request.POST:
        form = TaskForm(request.POST, initial={'user': request.user})
        print(f"di luar {form.is_valid()}")
        if form.is_valid():
            print(f"di dalem {form.is_valid()}")
            form.save()
            return HttpResponse("ok")
        else:
            print(form.errors.as_data())

    return render(request, 'create_task.html', {'form': TaskForm})


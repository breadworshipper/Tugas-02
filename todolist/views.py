from django.shortcuts import render
from todolist.models import Task
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from todolist.forms import TaskForm
from django.contrib.auth.decorators import login_required
from bootstrap_modal_forms.generic import BSModalCreateView



todo_list_data = Task.objects.all().values()

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todo_list(request):
    user_data = Task.objects.filter(user=request.user).values()
    context = {
        'todo_list': user_data,  # data untuk HTML
        'nama': request.user.username,
        'user': request.user,
        'form' : TaskForm,
    }
    return render(request, 'todolist.html', context)

def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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
        form = TaskForm(request.POST)
        print({form.is_valid()})
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            return HttpResponseRedirect('/todolist/')
        else:
            print(form.errors.as_data())

    return render(request, 'create_task.html', {'form': TaskForm})


def add_task(request):
    # Dari solusi LAB
    if request.POST:
        title = request.POST.get("tasktitle")
        description = request.POST.get("description")

        new_task = Task()
        new_task.user = request.user
        new_task.title = title
        new_task.description = description
        new_task.save()

    return HttpResponseNotFound()



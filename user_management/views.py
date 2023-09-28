from django.shortcuts import render, redirect
from .models import User
from .forms import UserRegistrationForm

def create_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_form.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_management/user_list.html', {'users': users})

def edit_user(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserRegistrationForm(instance=user)
    return render(request, 'user_management/user_form.html', {'form': form})

def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('user_list')

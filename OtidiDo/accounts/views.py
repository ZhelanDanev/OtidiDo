from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404

from OtidiDo.accounts.forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required

from OtidiDo.accounts.models import Traveler


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматично логване след регистрация
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    traveler = Traveler.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'traveler': traveler})


@login_required
def profile_detail(request, pk):
    traveler = get_object_or_404(Traveler, pk=pk)
    return render(request, 'accounts/profile.html', {'traveler': traveler})


@login_required
def edit_profile(request):
    traveler = Traveler.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=traveler)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=traveler)
    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')

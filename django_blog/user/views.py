from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
    if request.method =='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Your Account has been created ! You can log in.')
            return redirect('login')

    
    else:
        form=UserRegistrationForm()
    return render(request,'user/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'user/profile.html')
from django.shortcuts import render
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect

def signup_view(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("items:list_items")
    else:
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    
    if request.method == 'POST':
        form = LoginForm(data= request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("items:list_items") 
        
    
    else:
        form = LoginForm()
        
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('items:list_items')
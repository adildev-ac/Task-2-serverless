from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def index(request):
    """Root index: redirect to signup to avoid 404 at '/'"""
    return redirect('signup')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.profile.role == 'Doctor':
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
        else:
            error = "Invalid credentials"
            return render(request, 'accounts/login.html', {'error': error})
    return render(request, 'accounts/login.html')

@login_required
def doctor_dashboard(request):
    profile = request.user.profile
    return render(request, 'accounts/doctor_dashboard.html', {'profile': profile, 'user': request.user})

@login_required
def patient_dashboard(request):
    profile = request.user.profile
    return render(request, 'accounts/patient_dashboard.html', {'profile': profile, 'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')

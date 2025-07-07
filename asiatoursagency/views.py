from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from .models import tour
from .form import ContactForm, RegisterForm

# Create your views here.
def index(request):
    tours = tour.objects.all()
    context = {'tours': tours}
    return render(request, 'tours/index.html', context)

def Home_View(request):
    return render(request, 'tours/index.html')

def Contact_View(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.SendEmail()
            return redirect('contact-success')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'tours/contact.html', context)

def Contact_Success_View(request):
    return render(request, 'tours/contact-success.html')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists. Please choose another one.")
            else:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect('index')
    else:
        form = RegisterForm()

    return render(request, 'tours/register.html', {'form': form})

def login_view(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'index'
            return redirect(next_url)
        else:
            error_message = "Invalid Credentials!"
    return render(request, 'accounts/login.html', {'error': error_message})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('index')

@login_required
def home_view(request):
    return render(request, 'tours/index.html')

class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'registration/Protected.html')

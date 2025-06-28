from django.shortcuts import render, redirect
from .models import tour
from .form import ContactForm

# Creat your views here.
def index(request):
    tours = tour.objects.all()
    context = {'tours':tours}
    return render(request, 'tours/index.html', context)

#This Is The Home Page Function
def Home_View(request):
    return render(request, 'tours/index.html')

#This Is To define The Contact Func To Handle The Contact Form
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
        
#Define The Contact_Success_View
def Contact_Success_View(request):
    return render(request, 'tours/contact-success.html')
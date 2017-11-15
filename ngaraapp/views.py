from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Index
from .models import About
from .models import Service
from .models import Contact
from ngaraapp.form import ContactForm

from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
       
class AboutPageView(TemplateView):
    template_name = "about.html"
    
class ServicePageView(TemplateView):
    template_name = "service.html"
    
class ContactPageView(TemplateView):
     template_name = "contact.html"

     def get(self, request):
         form = ContactForm()
         return render(request, self.template_name, {'form': form})        

     def post(self, request):
         form = ContactForm(request.POST) 
         if form.is_valid():
            form.save()
         return redirect(request.path_info)   

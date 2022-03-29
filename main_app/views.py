from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View #View class to handle requests
from django.http import HttpResponse 

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

    # Old get
    # def get(self, request):
    #     #Returning string that says "Cats Home"
    #     return HttpResponse("Finches Home")

class About(TemplateView):
    template_name = 'about.html'


    # Old get 
    # def get(self, request):
    #     return HttpResponse("Finches About")


class Finch:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


finches = [
    Finch("birb", 3, "Male"),
    Finch("girl", 5, "Female"),
    Finch("boy", 6, "Male"),

]

class Finch_List(TemplateView):
    template_name = 'finchlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['finches'] = finches
        return context

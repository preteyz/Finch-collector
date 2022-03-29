from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views import View #View class to handle requests
from django.http import HttpResponse 
from .models import Finch


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

    # Old get
    # def get(self, request):
    #     #Returning string that says "Finchs Home"
    #     return HttpResponse("Finches Home")

class About(TemplateView):
    template_name = 'about.html'


    # Old get 
    # def get(self, request):
    #     return HttpResponse("Finches About")

# class Finch:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender


class Finch_List(TemplateView):
    template_name = 'finchlist.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["finches"] = Finch.objects.all()
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["finches"] = Finch.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["finches"] = Finch.objects.all()
            context["header"] = "Our Cats"
        return context


class Finch_Create(CreateView):
    model = Finch
    fields = ['name', 'img', 'age', 'gender']
    template_name = "finch_create.html"
    success_url = "/finches/"
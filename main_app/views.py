from nis import cat
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views import View #View class to handle requests
from django.http import HttpResponse , HttpResponseRedirect
from .models import Finch, FinchToy
from django.urls import reverse



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
            context["header"] = "Our Finches"
        return context


class Finch_Create(CreateView):
    model = Finch
    fields = ['name', 'img', 'age', 'gender', 'user', 'finchtoys']
    template_name = "finch_create.html"
    # success_url = "/finches/"
    # def get_success_url(self) -> str:
    #     return reverse('finch_detail', kwargs={'pk': self.object.pk})
    # model = Finch
    # fields = '__all__'
    # success_url = '/finches'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/finches')

class Finch_Detail(DetailView):
    model = Finch
    template_name= "finch_detail.html"

class Finch_Update(UpdateView):
    model = Finch
    fields = ['name', 'img', 'age', 'gender', 'user', 'finchtoys']
    template_name = "finch_update.html"
    # success_url = "/finches"
    def get_success_url(self) -> str:
        return reverse('finch_detail', kwargs={'pk': self.object.pk})

class Finch_Delete(DeleteView):
    model = Finch
    template_name = "finch_delete_confirmation.html"
    success_url = "/finches"

def profile(request, username):
    user = User.objects.get(username=username)
    finches = Finch.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username,'finches': finches})

#Finch Toys

def finchtoys_index(request):
    finchtoys = FinchToy.objects.all()
    return render(request, 'finchtoy_index.html', {'finchtoys': finchtoys})

def finchtoys_show(request, finchtoy_id):
    finchtoy = FinchToy.objects.get(id=finchtoy_id)
    return render(request, 'finchtoy_show.html', {'finchtoy': finchtoy})

class Finch_Toy_Create(CreateView):
    model = FinchToy
    fields = '__all__'
    template_name = "finchtoy_form.html"
    success_url = '/finchtoys'

class Finch_Toy_Update(UpdateView):
    model = FinchToy
    fields = ['name', 'color']
    template_name = "finchtoy_update.html"
    success_url = '/finchtoys'

class Finch_Toy_Delete(DeleteView):
    model = FinchToy
    template_name = "finchtoy_confirm_delete.html"
    success_url = '/finchtoys'

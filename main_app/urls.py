from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('about/', views.About.as_view(), name = "about"),
    path('finches/', views.Finch_List.as_view(), name= "finch_list" ),
    path('finches/new/', views.Finch_Create.as_view(), name = "finch_create"),
    path('finches/<int:pk>/', views.Finch_Detail.as_view(), name="finch_detail"),
] 
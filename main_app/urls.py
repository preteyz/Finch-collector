from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('about/', views.About.as_view(), name = "about"),
    path('finches/', views.Finch_List.as_view(), name= "finch_list" ),
    path('finches/new/', views.Finch_Create.as_view(), name = "cat_create"),
    # path('cats/<int:pk>/', views.CatDetail.as_view(), name="cat_detail"),
] 
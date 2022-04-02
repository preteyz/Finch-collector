from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('about/', views.About.as_view(), name = "about"),
    path('finches/', views.Finch_List.as_view(), name= "finch_list" ),
    path('finches/new/', views.Finch_Create.as_view(), name = "finch_create"),
    path('finches/<int:pk>/', views.Finch_Detail.as_view(), name="finch_detail"),
    path('finches/<int:pk>/update', views.Finch_Update.as_view(), name="finch_update"),
    path('finches/<int:pk>/delete', views.Finch_Delete.as_view(), name="finch_delete"),
    path('user/<username>', views.profile, name = "profile"),
    path('finchtoys/', views.finchtoys_index, name='finchtoys_index'),
    path('finchtoys/<int:finchtoy_id>', views.finchtoys_show, name='finchtoys_show'),
    path('finchtoys/create/', views.Finch_Toy_Create.as_view(), name='finchtoys_create'),
    path('finchtoys/<int:pk>/update/', views.Finch_Toy_Update.as_view(), name='finchtoys_update'),
    path('finchtoys/<int:pk>/delete/', views.Finch_Toy_Delete.as_view(), name='finchtoys_delete'),


] 
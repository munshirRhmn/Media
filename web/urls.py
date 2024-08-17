from django.urls import path,include
from .import views

app_name = "web"

urlpatterns = [
    path("",views.index,name='index'),
    path("result_show",views.result_show,name='result_show'),
    path('edit/<slug:slug>/', views.edit, name='edit'),
    path('delete/<slug:slug>/', views.delete, name='delete'),
]

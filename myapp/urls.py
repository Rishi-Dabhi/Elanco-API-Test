from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('applications/', views.applications, name = 'applications'),
    path('applications/selectApp/<str:app>', views.select_app_name, name ='select_app_name'),
    path('resources',views.resources, name='resources'),
    path('resources/selectResource/<str:res>',views.select_resource_name, name="select_resource_name"),
]
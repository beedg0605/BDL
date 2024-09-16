from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path('tech_stack',views.tech_stack,name="tech_stack"),
    path('project',views.project, name="project"),
    path('contact',views.contact,name="contact")
]
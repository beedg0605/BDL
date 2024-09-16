from django.shortcuts import render
from . social_links import get_social_links
# Create your views here.
def index(request):
    links = get_social_links()
    context = {'links':links}
    return render(request, 'index.html', context)

def tech_stack(request):
    return render(request, 'tech_stack.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    return render(request, 'contact.html')

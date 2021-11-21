from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def report(request): 
    return render(request = request, template_name = "contact.html")
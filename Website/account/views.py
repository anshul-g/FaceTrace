from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout 
from facetrace.models import CustomUser
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def account(request): 
	args = {'user': request.user}
	return render(request, "settings.html", args)

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/")
from django.shortcuts import render

# Create your views here.
def reset(request):
    return render(request, 'reset.html')
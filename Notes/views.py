from django.shortcuts import render


# Create your views here.

def landing_page(request):


    context = {"context": "Welcome to MindVault"}
    return render(request, "index.html", context)

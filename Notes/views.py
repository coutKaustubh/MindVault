from django.shortcuts import render


# Create your views here.

def notes_entry(request):

    
    context = {"context": "Welcome to MindVault"}
    return render(request, "index.html", context)

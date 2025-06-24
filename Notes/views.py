from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render(request, "index.html")


def notes_entry(request):
    topics = Topic.objects.all()
    entries = Entry.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        # Handle Topic creation
        if form_type == 'add_topic':
            topic_name = request.POST.get('topic')
            if topic_name:
                Topic.objects.create(name=topic_name)
            return redirect('/MindVault/')

        # Handle Note creation
        elif form_type == 'add_note':
            topic_id = request.POST.get('selected_topic')
            title = request.POST.get('title')
            description = request.POST.get('description')
            image = request.FILES.get('image')

            try:
                topic = Topic.objects.get(id=topic_id)
                Entry.objects.create(
                    topic=topic,
                    title=title,
                    description=description,
                    image=image
                )
            except Topic.DoesNotExist:
                pass

            return redirect('/MindVault/')

    return render(request, 'home.html', {
        'topics': topics,
        'entries': entries
    })

def login_page(request):

    if request.method != 'POST':
        return render(request , "login.html")

    username = request.POST.get('username')
    password = request.POST.get('password')
    
    if not User.objects.filter(username=username).exists():
        messages.error(request,'Invalid Username')
        return redirect('/login/')
    
    user = authenticate(username=username,password=password)
    if user is None:
        messages.error(request , 'Invalid Password')
        return redirect('/login/')
    
    else:
        login(request , user)
        return redirect('/MindVault/')


def register(request):
    return render(request , "register.html")
import feedparser
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from gallery.models import Photo

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'O usuário não esta logado.')
        return redirect('users_login')
    cards = Photo.objects.order_by("created_at").filter(publish=True)
    return render(request, 'gallery/index.html', {"cards": cards})

def image(request, id):
    photo = get_object_or_404(Photo, pk=id)
    return render(request, 'gallery/image.html', {'photo':photo})

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'O usuário não esta logado.')
        return redirect('users_login')
    cards = Photo.objects.order_by("created_at").filter(publish=True)
    
    if "search" in request.GET:
        data = request.GET["search"]
        if data:
            cards = cards.filter(name__icontains=data)
    return render(request, "gallery/search.html", {"cards": cards})

def filter_by_category(request, category):
    cards = Photo.objects.order_by("created_at").filter(publish=True).filter(category=category)
    return render(request, 'gallery/search.html', {'cards': cards })

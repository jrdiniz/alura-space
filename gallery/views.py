from django.shortcuts import render
from django.shortcuts import get_object_or_404
from gallery.models import Photo

def index(request):
    cards = Photo.objects.all()
    return render(request, 'gallery/index.html', {"cards": cards})

def image(request, id):
    photo = get_object_or_404(Photo, pk=id)
    return render(request, 'gallery/image.html', {'photo':photo})
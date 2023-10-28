from django.urls import path
from gallery.views import index
from gallery.views import image

urlpatterns = [
    path("", index, name='index'),
    path("image/<int:id>", image, name='image')
]

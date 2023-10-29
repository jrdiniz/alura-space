from django.urls import path
from gallery.views import index
from gallery.views import image
from gallery.views import search
from gallery.views import filter_by_category

urlpatterns = [
    path("", index, name='index'),
    path("image/<int:id>", image, name='image'),
    path("search", search, name="search"),
    path("filter/<str:category>", filter_by_category, name="filter"),
]

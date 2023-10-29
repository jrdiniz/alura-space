from django.contrib import admin
from gallery.models import Photo

class ListPhotos(admin.ModelAdmin):
    list_display = ("id", "name", "credit", "publish")
    list_display_links = ("id", "name")
    search_fields = ("name", )
    list_filter = ("category", )
    list_editable = ("publish", )
    list_per_page = 10
    readonly_fields = ('display_photo', )

admin.site.register(Photo, ListPhotos)

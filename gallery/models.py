from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.html import format_html

# Create your models here.
class Photo(models.Model):
    
    CATEGORIES = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALAXIA", "Galaxia"),
        ("PLANETA", "Planeta")
    ]
    
    name = models.CharField(max_length=100, null=False, blank=False)
    credit = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False, choices=CATEGORIES, default="")
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now(), blank=False)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    
    def __str__(self):
        return self.name
    
    @cached_property
    def display_photo(self):
        html = '''
            <img src="{img}" width="640">
        '''
        if self.photo:
            return format_html(html, img=self.photo.url)
        return format_html('<strong>Nenhuma foto disponível.</strong>')
    display_photo.short_description = 'Display photo'
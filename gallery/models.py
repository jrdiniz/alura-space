from django.db import models
from django.utils import timezone

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
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    category = models.CharField(max_length=100, null=False, blank=False, choices=CATEGORIES, default="")
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now(), blank=False)
    
    def __str__(self):
        return self.name
    
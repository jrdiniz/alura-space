from django.db import models

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
    photo = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False, choices=CATEGORIES, default="")
    
    def __str__(self):
        return self.name
    
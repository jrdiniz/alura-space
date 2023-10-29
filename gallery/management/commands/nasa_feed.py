import feedparser
import random
import requests
import os
from pathlib import Path
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from django.core.files.uploadedfile import UploadedFile
from django.conf import settings
from gallery.models import Photo

class Command(BaseCommand):
    help = "Import images from Nasa Feed"
    
    def handle(self, *args, **kwargs):
        feed = feedparser.parse("https://www.nasa.gov/feeds/iotd-feed/")
        
        categories = ['NEBULOSA','PLANETA','ESTRELA','GALAXIA']
        
        today = datetime.now()
        
        for image in feed['entries']:
            if image['description']:
                filename = image['links'][1]['href'].split("/")[-1]
                data = Photo(
                    name = image['title'],
                    description = image['description'],
                    category = random.choice(categories),
                    credit=image['source']['title'],
                    publish=True
                )
                image_file = requests.get(image['links'][1]['href']).content                
                path = settings.MEDIA_ROOT + f"/photo/{filename}"
                with open(path, 'wb') as handler:
                    handler.write(image_file)
                data.photo.save(filename, UploadedFile(file=open(path, 'rb')))
                os.remove(path)
                                    
        self.stdout.write(
            self.style.SUCCESS('OK !!!')
        )
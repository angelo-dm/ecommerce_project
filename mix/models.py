from django.db import models
from django.utils.html import mark_safe

class Produto(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    detalhes = models.TextField()
    image = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return self.name
    
    def image_admin(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="80" />')
        else:
            return "No image"
        
    image_admin.short_description = 'Image'
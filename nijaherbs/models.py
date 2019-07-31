from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.
class Category(models.Model):
    """Model representing a herb category."""
    name = models.CharField(max_length=200, help_text='Enter a herb category (e.g. Medicinal)')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Region(models.Model):
    """Model representing region popular."""
    name = models.CharField(max_length=200, help_text='Enter a region (e.g. Yoruba)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Herb(models.Model):
    image = models.ImageField(upload_to = 'images/', blank=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the herb')
    description	= models.TextField(help_text='Enter description of the herb', null=True)
    health_benefits	= models.TextField(help_text='Enter the health benefits of the of the herb', null=True)
    uses	= models.TextField(help_text='Enter uses of the herb', null=True)
    local_Name = models.CharField(max_length=200)
    english_Name = models.CharField(max_length=200)
    botanical_Name = models.CharField(max_length=200)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        """String for representing the Model object."""
        return self.local_Name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this herb."""
        return reverse('herb', args=[str(self.id)])
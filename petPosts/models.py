from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User  

# Create your models here.


POST_TYPES = (
    (1, 'Se perdió mi mascota'),
    (2, 'Encontré una mascota perdida'),
    (3, 'Doy mascota en tránsito/adopción'),
    (4, 'Quiero adoptar/transitar una mascota'),
    (5, 'Necesito ayuda con una mascota')
)


class PetType(models.Model):
    pet_type = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.pet_type


class Color(models.Model):
    color = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.color


class Area(models.Model):
    area = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['area']

    def __str__(self):
        return self.area
    

class PetPost(models.Model):
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_type = models.ManyToManyField(PetType, related_name='pet_types')
    other_pet_type = models.CharField(max_length=20, blank=True, null=True)
    pet_qty = models.IntegerField(default=1)
    pet_color = models.ManyToManyField(Color, related_name='pet_colors')
    other_pet_color = models.CharField(max_length=20, blank=True, null=True)
    pet_name = models.CharField(max_length=20, blank=True, null=True)
    post_type = models.IntegerField(choices=POST_TYPES)
    area = models.ManyToManyField(Area, related_name='pet_area', default='ROSARIO')
    other_area = models.CharField(max_length=20, blank=True, null=True)
    post_title = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
    post_message = models.CharField(max_length=500, validators=[MinLengthValidator(10)])
    post_img01 = models.ImageField(upload_to='post_images/')
    post_img02 = models.ImageField(upload_to='post_images/', blank=True, null=True)
    post_img03 = models.ImageField(upload_to='post_images/', blank=True, null=True)
    post_likes = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-post_date', '-post_likes']
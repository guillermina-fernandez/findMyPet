from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User  

# Create your models here.


POST_TYPES = (
    (1, 'Se perdió mi mascota'),
    (2, 'Encontré una mascota perdida'),
    (3, 'Necesito ayuda con una mascota'),
)


class Color(models.Model):
    color = models.CharField(max_length=20, unique=True)

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
    pet_color = models.ManyToManyField(Color, related_name='pet_colors')
    pet_name = models.CharField(max_length=20, blank=True, null=True)
    post_type = models.IntegerField(choices=POST_TYPES)
    area = models.ManyToManyField(Area, related_name='pet_area')
    other_area = models.CharField(max_length=20, blank=True, null=True)
    post_message = models.CharField(max_length=500, validators=[MinLengthValidator(10)])
    post_img01 = models.ImageField(upload_to='post_images/')
    post_img02 = models.ImageField(upload_to='post_images/', blank=True, null=True)
    post_img03 = models.ImageField(upload_to='post_images/', blank=True, null=True)
    post_likes = models.IntegerField(default=0)
    
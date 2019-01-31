from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from location_field.models.plain import PlainLocationField
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)




class Post(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	main_Image = models.ImageField(blank=True,null=True)
	sub_Image_1 = models.ImageField(blank=True,null=True)
	sub_Image_2 = models.ImageField(blank=True,null=True)
	

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})
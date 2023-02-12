from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Blogpost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50 , default='')
    title = models.CharField(max_length=100)
    heading = models.CharField(max_length=100)
    h1_content = models.TextField()
    sub_heading = models.CharField(max_length=100)
    h2_content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    audio = models.FileField(upload_to='audioFiles',default='song.mp3')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog post' , kwargs={'pk':self.pk})


    
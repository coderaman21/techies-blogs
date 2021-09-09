from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE)
    image = models.ImageField(upload_to = 'profile_pics',default='default.png')

    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height>300 or img.width>300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
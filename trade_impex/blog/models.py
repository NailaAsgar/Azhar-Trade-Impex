from django.db import models
from django.utils import timezone
from django.urls import reverse



# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=False, unique= True)


    


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return '/'+self.title+ '/'
        return reverse('post_detail', kwargs={'slug': self.slug})
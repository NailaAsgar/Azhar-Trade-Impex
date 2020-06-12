from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post

class StaticViewSitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['blog-home', 
        'blog-about', 
        'blog-white', 
        'blog-blue', 
        'blog-orange', 
        'blog-silica_gel_bag', 
        'blog-silica_gel_pouch', 
        'blog-FAQ']

    def location(self, item):
        return reverse(item)

class Post_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Post.objects.all()

    


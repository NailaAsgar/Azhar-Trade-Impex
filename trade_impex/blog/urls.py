from django.contrib import admin
from django.urls import path, include
from .import views
from .views import PostDetailView, PostListView

urlpatterns = [
    
    path('', views.home, name = 'blog-home'),
    path('contact/',views.contact, name = 'blog-contact'),
    path('about/',views.about, name = 'blog-about'),
    path('blue/',views.blue, name = 'blog-blue'),
    path('orange/',views.orange, name = 'blog-orange'),
    path('white/',views.white, name = 'blog-white'),
    path('silica_gel_bag/',views.silica_gel_bag, name = 'blog-silica_gel_bag'),
    path('silica_gel_pouch/',views.silica_gel_pouch, name = 'blog-silica_gel_pouch'),
    path('FAQ/',views.FAQ, name = 'blog-FAQ'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'post-detail'),
    path('post/',PostListView.as_view(), name = 'post'),

]

from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Post
from django.core.mail import send_mail
from django.views.generic import DetailView, ListView

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        content = request.POST['content']

        send_mail(
            subject,
            content,
            email,
            ['kaziazhar04@gmail.com'],
        )

        return render(request, 'blog/contact.html', {'name':name})
    else:
        return render(request, 'blog/contact.html')

def about(request):
    return render(request, 'blog/about.html')

def blue(request):
    return render(request, 'blog/blue.html')

def orange(request):
    return render(request, 'blog/orange.html')

def white(request):
    return render(request, 'blog/white.html')

def silica_gel_bag(request):
    return render(request, 'blog/silica-gel-bag.html')

def silica_gel_pouch(request):
    return render(request, 'blog/silica-gel-pouch.html')

def FAQ(request):
    return render(request, 'blog/FAQ.html')

def b_home(request):
    args = {
        'posts' : Post.objects.all()
       }
    return render(request, 'blog1/home.html',args)

# def Detailview(request):
#     context = {
#         'posts' : Post.objects.all()
#     # }
#     # return render(request, 'blog/post_detail.html' , context)

class PostListView(ListView):
    model = Post
    template_name = 'blog1/home.html'
    context_object_name = 'posts'
    ordering = ('-date_posted')
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'











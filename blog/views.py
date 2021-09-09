from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import Blogpost
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.

def index(request):
    posts = Blogpost.objects.all()
    return render(request,'blog/index.html',{'blogpost':posts})

# class based view
# this will work as index function above
class PostListView(ListView):
    model = Blogpost
    template_name = 'blog/index.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'blogpost'
    ordering = ['date'] 
    
    # for pagination (paginate_by is a default variable)
    paginate_by = 4


# to dispaly  a users all posts 
class UserPostListView(ListView):
    model = Blogpost
    template_name = 'blog/user_posts.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'blogpost'
    # for pagination (paginate_by is a default variable)
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        return Blogpost.objects.filter(author=user).order_by('-date')

# to display all posts by a category
class CategoryPostListView(ListView):
    model = Blogpost
    template_name = 'blog/category_posts.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'blogpost'
    # for pagination 
    paginate_by = 5

    def get_queryset(self):   
        posts = Blogpost.objects.filter(category=self.kwargs.get('category'))
        return posts

def blogpost(request,name):
    posts = Blogpost.objects.filter(title = name)
    return render(request,'blog/blogpost.html',{'posts':posts})

# PostDetailView class will work same as blogpost function above
class PostDetailView(DetailView):
    model = Blogpost
    template_name = 'blog/blogpost.html'
    # context_object_name = 'posts'

      
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Blogpost
    # template = blogpost_form.html
    fields = ['category','title','heading','h1_content','sub_heading','h2_content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Blogpost

    fields = ['category','title','heading','h1_content','sub_heading','h2_content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Blogpost
    
    success_url = '/'
    # template = blogpost_confirm_delete.html

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

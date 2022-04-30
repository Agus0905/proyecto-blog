from dataclasses import fields
from unicodedata import category
from urllib import request
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post, Comment
from .forms import PostForm, UpdateForm, CommentForm
from django.http import HttpResponseRedirect
# Create your views here.

#def home(request):
 #   return render(request, 'home.html')

class search_bar(ListView):
    model = Post
    template_name = 'search_bar.html'
    ordering = ['-post_date']
    
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list

#def search_bar(request):
    #if request.method == 'POST':
    # searched = request.POST['searched']
    # post = Post.objects.filter(title__contains=searched)
    # return render(request, 'search_bar.html', {'searched':searched, 'post':post})
    #else:
  #   return render(request, 'search_bar.html', {})
#
  #  return HttpResponseRedirect(reverse('blog-detail', args=[str(pk)]))


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
     post.likes.remove(request.user)
     liked = False
    else:
     post.likes.add(request.user)
     liked = True
    
    return HttpResponseRedirect(reverse('blog-detail', args=[str(pk)]))



class Homeview(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Homeview, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})


def CategoryView(request, cats):
    category_posts =  Post.objects.filter(category = cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts': category_posts})

class BlogDetailview(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogDetailview, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')  No anda(NO USAR)
    def create(request):
     if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) 

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')

class UpdatePost(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryPost(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

def Aboutpage(request):
    return render(request, 'about.html')
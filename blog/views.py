from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class Blog(ListView):
    model = Post
    template_name = 'blog/blog.html'


class ArticleDetail(DetailView):
    model = Post
    template_name = 'blog/article-details.html'

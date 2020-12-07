from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Post


class Blog(ListView):
    model = Post
    template_name ='blog/blog.html'

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment
from .forms import AddComment


class Blog(ListView):
    model = Post
    template_name = 'blog/blog.html'


class ArticleDetail(DetailView):
    model = Post
    template_name = 'blog/article-details.html'


class NewComment(CreateView):
    model = Comment
    form_class = AddComment

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

from django.urls import path
from.views import Blog, ArticleDetail


urlpatterns = [
    path('', Blog.as_view(), name="blog"),
    path('article/<int:pk>', ArticleDetail.as_view(), name="article-detail"),
]

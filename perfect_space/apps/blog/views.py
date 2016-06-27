# coding=utf-8
from django.views.generic import ListView, DetailView
from perfect_space.apps.blog.models import Post
from perfect_space.apps.pages.models import Page


class BlogDetail(DetailView):
    model = Post
    context_object_name = 'page'
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_similar'] = Post.objects.all()[:3]
        return context


class BlogList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/list.html'
    slug = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Page.objects.get(slug=self.slug)
        return context
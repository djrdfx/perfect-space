# coding=utf-8
from django.views.generic import DetailView, ListView
from perfect_space.apps.pages.models import Page
from perfect_space.apps.projects.models import Project


class ProjectDetail(DetailView):
    model = Project
    context_object_name = 'page'
    template_name = 'projects/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects_similar'] = Project.objects.all()[:3]
        return context


class ProjectList(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/list.html'
    slug = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Page.objects.get(slug=self.slug)
        return context
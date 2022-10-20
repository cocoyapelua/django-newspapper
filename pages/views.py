from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
from articles.models import Article
from accounts.models import CustomUser


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.select_related('author').all().order_by('-date')[:3]
        return context

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
from articles.models import Article
from accounts.models import CustomUser


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = Article.objects.all().order_by('-date')
        context['latest_articles'] = article
        context['user_data'] = CustomUser.objects.get(pk=article[0].author_id)
        return context

from django.shortcuts import render
from .models import Artiles


def news_home(request):
    news = Artiles.objects.order_by('data')
    return render(request, 'news/news_home.html', {'news': news})

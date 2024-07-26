from django.shortcuts import render
from .models import ArticleIndexPage, ArticlePage

def article_index(request):
    articles = ArticlePage.objects.live().public()  
    context = {
        'page': ArticleIndexPage.objects.live().public().first(), 
        'articles': articles,
    }
    return render(request, 'articles/article_index_page.html', context)

def article_page(request, slug):
    article = ArticlePage.objects.filter(slug=slug).first()
    if not article:
        # Handle the case where the page is not found (e.g., return a 404)
        pass 
    
    context = {
        'page': article,
    }
    return render(request, 'articles/article_page.html', context)

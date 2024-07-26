

# articles/urls.py

from django.urls import path
from wagtail.views import serve

urlpatterns = [
    path('', serve, name='article_index'),  # Use Wagtail's serve view
    path('<slug:slug>/', serve, name='article_page'),
]
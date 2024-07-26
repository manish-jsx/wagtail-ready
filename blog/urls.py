

# blog/urls.py
from django.urls import path
from wagtail.views import serve

urlpatterns = [
    path('', serve, name='blog_index'),  
    path('<slug:slug>/', serve, name='blog_page'),
]

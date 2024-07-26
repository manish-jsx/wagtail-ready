

# from django.urls import path

# from wagtail.model import serve

# urlpatterns = [
#     path('', serve, name='blog_index'),  # Use Wagtail's `serve` view
#     path('<slug:slug>/', serve, name='blog_page'),  # Use Wagtail's `serve` view
# ]

# blog/urls.py
from django.urls import path
from wagtail.views import serve

urlpatterns = [
    path('', serve, name='blog_index'),  
    path('<slug:slug>/', serve, name='blog_page'),
]

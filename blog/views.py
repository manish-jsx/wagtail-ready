# blog/views.py


# blog/views.py

from .models import BlogPage

class BlogPageView(BlogPage):
    def get_context(self, request, *args, **kwargs):
        # You can add any custom context data here
        context = super().get_context(request, *args, **kwargs)
        return context

from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class BlogIndexPage(Page):
    """Blog index page model. This serves as the parent page for your blog posts."""

    intro = RichTextField(
        blank=True,
        features=["h2", "h3", "bold", "italic", "link", "ol", "ul"]
    )

    # Restrict the number of BlogIndexPage instances to 1
    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
    ]

    # Specify the allowed subpage types for this page
    subpage_types = ["blog.BlogPage"]

    def get_context(self, request, *args, **kwargs):
        """Add custom data to the context for the blog index page."""
        context = super().get_context(request, *args, **kwargs)

        # Get all live and public blog posts that are descendants of this page
        blogpages = self.get_children().live().public()
        context["blogpages"] = blogpages

        return context


class BlogPage(Page):
    """Individual blog page model."""

    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body", classname="full"),
    ]

    # Specify the allowed parent page types for this page
    parent_page_types = ["blog.BlogIndexPage"]

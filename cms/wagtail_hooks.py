# myapp/wagtail_hooks.py
from wagtail.core import hooks
from wagtail.admin.ui.components import Component

from blog.models import BlogPage,BlogIndexPage
from articles.models import ArticlePage,ArticleIndexPage


@hooks.register('register_page_listing_buttons')
def add_page_listing_buttons(page, page_perms, is_parent=False):
    if page_perms.can_add_subpage():
        # Adding 'Blog' page button
        yield Component('wagtailadmin/shared/page_listing_buttons/button_with_dropdown.html', {
            'label': 'New Page',
            'attrs': {
                'title': "New Page",
                'aria-label': "New Page",
                'data-controller': "w-dropdown",
                'href': "#",
            },
            'items': [
                {
                    'label': "Blog",
                    'url': page.url + BlogPage.get_create_url_query_string(),
                    'classname': 'button button-small button-secondary w-dropdown__item',
                },
                {
                    'label': "Article",
                    'url': page.url + ArticlePage.get_create_url_query_string(),
                    'classname': 'button button-small button-secondary w-dropdown__item',
                },
                
            ]
        }, priority=10)
    
    

@hooks.register("before_edit_page")
def before_edit_page(request, page):
    print("Before editing page", page)  

@hooks.register("after_edit_page")
def after_edit_page(request, page):
    print("After editing page", page)


@hooks.register("before_create_page")
def before_create_page(request, parent_page, page_class):
    print("Before creating page", page_class)


@hooks.register("after_create_page")
def after_create_page(request, page):
    print("After creating page", page)


@hooks.register("before_publish_page")
def before_publish_page(request, page):
    print("Before publishing page", page)


@hooks.register("after_publish_page")
def after_publish_page(request, page):
    print("After publishing page", page)


@hooks.register("before_delete_page")
def before_delete_page(request, page):
    print("Before deleting page", page)


@hooks.register("after_delete_page")
def after_delete_page(request, page):
    print("After deleting page", page)

# Example: Adding a custom panel to the settings menu
@hooks.register("construct_settings_menu")
def hide_users_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name not in ["users"]]
    menu_items.append(Component(
    name="my_custom_panel",
    label="My Custom Panel",
    url="/admin/settings/my-custom-panel/",
    classnames="icon icon-cog",
    order=100  # Position in the menu
))


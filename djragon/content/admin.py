from django.contrib import admin

from django.conf import settings

from content.models import NewsArticle, Blog, Author #, CategorizedArticle
from content.forms import BlogForm, NewsArticleForm


class AuthorAdmin(admin.ModelAdmin):
    pass

class NewsArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = NewsArticleForm

'''
    class Media:
        js = [
            settings.TINYMCE_JS_URL,
            settings.TINYMCE_INIT_URL,
        ]
'''

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = BlogForm

'''
    class Media:
        js = [
            settings.TINYMCE_JS_URL,
            settings.TINYMCE_INIT_URL,

        ]
'''

admin.site.register(NewsArticle, NewsArticleAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
#admin.site.register(TaggedContent, TaggedContentAdmin)


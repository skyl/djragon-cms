from django.contrib import admin
from text_content.models import NewsArticle, Blog, Author


class AuthorAdmin(admin.ModelAdmin):
    pass

class NewsArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = [
            '/media/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/media/grappelli/tinymce_setup/tinymce_setup.js',
        ]


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = [
            '/media/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/media/grappelli/tinymce_setup/tinymce_setup.js',
        ]

admin.site.register(NewsArticle, NewsArticleAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)


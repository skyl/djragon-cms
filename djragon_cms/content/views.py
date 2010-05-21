from django.http import HttpResponse

from django.views.generic.list_detail import object_list
from django.shortcuts import render_to_response

from content.models import NewsArticle, Blog


def news_front_page(request, *args, **kwargs):
    '''has latest and most popular articles, featured'''

    page = request.GET.get('page')

    return object_list(request,
        queryset=NewsArticle.objects.all(),
        template_object_name='latest',
        paginate_by=10,
        page=page if page else 1,
        template_name='content/front_page.html',
        extra_context={
            #'most_popular': popular
        }
    )

def blog_front_page(request, *args, **kwargs):
    ''''''
    page = request.GET.get('page')

    return object_list(request,
        queryset=Blog.objects.all(),
        template_object_name='latest',
        paginate_by=10,
        page=page if page else 1,
        template_name='content/front_page.html',
        extra_context={
            #'most_popular': popular
        }
    )


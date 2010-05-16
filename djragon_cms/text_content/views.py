from django.http import HttpResponse

from django.views.generic.list_detail import object_list
from django.shortcuts import render_to_response

from text_content.models import NewsArticle


def news_front_page(request, *args, **kwargs):
    '''http://mis-asia.com/

    plugged into '/', has latest and most popular articles, featured'''

    page = request.GET.get('page')

    return object_list(request,
        queryset=NewsArticle.objects.all(),
        template_object_name='latest',
        paginate_by=10,
        page=page if page else 1,
        template_name='text_content/front_page.html',
        extra_context={
            #'most_popular': popular
        }
    )

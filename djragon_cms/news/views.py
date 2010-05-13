from django.http import HttpResponse

from django.views.generic.list_detail import object_list
from django.shortcuts import render_to_response

from news.models import Entry


def front_page(request):
    '''http://mis-asia.com/

    plugged into '/', has latest and most popular articles, featured'''

    page = request.GET.get('page')
    


    return object_list(request,
        queryset=Entry.objects.all(),
        template_object_name='latest',
        paginate_by=10,
        page=page if page else 1,
        template_name='news/front_page.html',
        extra_context={

        }
    )

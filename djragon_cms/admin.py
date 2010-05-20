from django.contrib import admin
from grappelli.sites import GrappelliSite

admin.site = GrappelliSite()
admin.autodiscover()

admin.site.groups = {
    0: {
        'name': 'Assets',
        'apps': ['content', 'page', 'tagging', 'comments'], #medialibrary
        'show_apps': True,
    },
    1: {
        'name': 'User Management',
        'apps': ['auth'],
        'classes': ['collapse-closed'],
        'show_apps': False,
    },
    2: {
        'name': 'Admin Interface Content',
        'apps': ['grappelli'],
        'classes': ['collapse-closed'],
        'show_apps': False,
    },
    3: {
        'name': 'Advanced',
        'apps': ['sites', 'transcode'],
        'classes': ['collapse-closed'],
        'show_apps': True,
    },
}

'''# hmmm can't get collections to work
admin.collections = {
    0: {
        'title': 'collection',
        'groups': [0,1],
    }
}
'''

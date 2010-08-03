from django.contrib import admin
from transcode.models import LogResult

class LogResultAdmin(admin.ModelAdmin):
    pass

admin.site.register(LogResult, LogResultAdmin)

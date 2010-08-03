from django.db import models

class LogResult(models.Model):
    '''Logs raw dumps from ffmpeg'''
    src_filepath = models.CharField(max_length=255)
    result_filepath = models.CharField(max_length=255)
    ffmpeg_result = models.TextField()
    success = models.BooleanField(default=True)
    datetime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s%s%s" % (self.datetime, self.src_filepath, self.result_filepath)


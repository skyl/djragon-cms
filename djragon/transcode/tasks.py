import datetime
import pexpect

from functools import partial as curry

from celery.decorators import task

from transcode.models import LogResult

from django.conf import settings
if hasattr(settings, 'TRANSCODE_LOCAL'):
    TRANSCODE_LOCAL = settings.TRANSCODE_LOCAL
else:
    TRANSCODE_LOCAL = False

@task(ignore_result=True)
def transcode_to_flv(src_filepath, result_filepath, width=320, height=240, **kwargs):
    logger = transcode_to_flv.get_logger(**kwargs)
    logger.info("\n Transcoding %s to flv" % src_filepath)
    child = pexpect.spawn('ffmpeg -i %s -ar 22050 -ab 32000 -f flv -s %sx%s %s' % (src_filepath, width, height, result_filepath),)
    #child.expect('Overwrite ? [y/N]', timeout=5)
    child.sendline('y')
    #callback = curry(foo.delay, child=child)
    ffmpeg_result = child.read()
    log_result.delay(ffmpeg_result, src_filepath, result_filepath) #callback=callback)
    logger.info('we just called log_result.delay')

@task(ignore_result=True)
def log_result(ffmpeg_result, src_filepath, result_filepath, callback=None, **kwargs):
    logger = log_result.get_logger(**kwargs)
    logger.info("\n logging the transcode")

    LogResult.objects.create(
        src_filepath=src_filepath,
        result_filepath=result_filepath,
        ffmpeg_result=ffmpeg_result,
    )

    if callback:
        callback(ffmpeg_result)

'''ffmpeg cheatsheet
-i input file name
-ar audio sampling rate in Hz
-ab audio bit rate in kbit/s
-f output format
-s output dimension

-i Input file name
-an disable audio
-r fps
-y overwrite file
-s output dimension

-ss record start time
-t record end time last for
'''

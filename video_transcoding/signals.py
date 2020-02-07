from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from video_transcoding import models, helpers


# noinspection PyUnusedLocal
@receiver(post_save, sender=models.Video)
def send_transcode_task(sender, *, instance: models.Video, created: bool, **kw):
    if not created:
        return
    transaction.on_commit(lambda: helpers.send_transcode_task(instance))

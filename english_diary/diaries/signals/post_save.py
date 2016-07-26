from django.db.models.signals import post_save
from django.dispatch import receiver

from diaries.models import Diary
from diaries.utils.words_cloud import save_wordcloud


@receiver(post_save, sender=Diary)
def post_save_diary(sender, instance, created, **kwargs):
    if created:
        save_wordcloud(instance.user)
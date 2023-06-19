from django.dispatch import receiver
from django.db.models.signals import m2m_changed
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives

from news.models import PostCategory
from django.conf import settings
from .tasks import notify_about_new_post


@receiver(m2m_changed, sender=PostCategory)
def task_notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        print('PRINT: ', instance.id)
        notify_about_new_post.apply_async([instance.id], countdown=10)


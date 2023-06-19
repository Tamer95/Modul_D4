from celery import shared_task
from .views import send_notifications, mailing_to_subs
from .models import Post, PostCategory
# from news.signals import send_notifications


@shared_task
def notify_about_new_post(instance_id):
    instance = Post.objects.get(pk=instance_id)
    categories = instance.post_category.all()
    subscribers: list[str] = []

    for category in categories:
        subscribers += category.subscribers.all()

    subscribers = [s.email for s in subscribers]
    print('PRINT: GUD!')

    send_notifications(instance.preview(), instance.pk, instance.post_name, subscribers)

@shared_task
def monday_mailing():
    mailing_to_subs()
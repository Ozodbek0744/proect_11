from uuid import uuid4
import random as r
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.dispatch import receiver
from account.models import Account



def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'blog/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class BlogModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)

    @property
    def image_url(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)


@receiver(pre_save, sender=BlogModel)
def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify((str(r.randint(1, 10000)) + "-" + str(r.randint(1, 10000))))


@receiver(post_delete, sender=BlogModel)
def delete_blog_image_from_media(sender, instance, *args, **kwargs):
    instance.image.delete()


class Comment(models.Model):
    description = models.TextField(max_length=800)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    blog = models.ForeignKey(BlogModel, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.description)


class Izoh(models.Model):
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comment, related_name='izoh', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.description)



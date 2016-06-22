from django.db import models

from users.models import User


class Post(models.Model):

    user = models.ForeignKey(User)

    video_id = models.CharField(
        max_length=16,
    )

    video_original_title = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )

    title = models.CharField(
        max_length=256,
    )

    content = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # TODO: youtube original url
    # TODO: youtube embed source code

    def __str__(self):
        return self.title

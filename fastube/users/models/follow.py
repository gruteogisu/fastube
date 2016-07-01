from django.db import models


class Follow(models.Model):
    follower = models.ForeignKey(
        "User",
        related_name="+",
    )
    followee = models.ForeignKey(
        "User",
        related_name="+",
    )

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

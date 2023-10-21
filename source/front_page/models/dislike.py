from django.contrib.auth import get_user_model
from django.db import models


class Dislike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    task = models.ForeignKey(
        "front_page.Task", null=True, blank=True, on_delete=models.CASCADE
    )
    comment = models.ForeignKey(
        "front_page.Comment", null=True, blank=True, on_delete=models.CASCADE
    )
    solution = models.ForeignKey(
        "front_page.Solution", null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        indexes = [
            models.Index(fields=["task"]),
            models.Index(fields=["comment"]),
            models.Index(fields=["solution"]),
        ]

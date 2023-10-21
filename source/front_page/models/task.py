import uuid

from django.db import models
from django.db.models import QuerySet

from front_page.models import Comment, Solution


class Task(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False)
    summary = models.CharField(max_length=128)
    task = models.TextField()
    date_of_task = models.DateField()

    def __str__(self) -> str:
        return self.summary

    @property
    def _get_reaction(self) -> int:
        from front_page.models import Dislike, Like

        like = Like.objects.filter(task=self).count()
        dislike = Dislike.objects.filter(task=self).count()

        return like - dislike

    def _get_comments(self) -> QuerySet[Comment]:
        return Comment.objects.filter(task=self).order_by("-created_at")

    def _get_solutions(self) -> QuerySet[Solution]:
        return Solution.objects.filter(task=self)

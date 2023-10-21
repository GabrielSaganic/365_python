import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet

from front_page.models import Comment


class Solution(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    solution = models.TextField()
    task = models.ForeignKey("front_page.Task", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.get_username()} - {self.task.summary}"

    @property
    def _get_reaction(self) -> int:
        from front_page.models import Dislike, Like

        like = Like.objects.filter(solution=self).count()
        dislike = Dislike.objects.filter(solution=self).count()

        return like - dislike

    def _get_comments(self) -> QuerySet[Comment]:
        return Comment.objects.filter(solution=self).order_by("-created_at")

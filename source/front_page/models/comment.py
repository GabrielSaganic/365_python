import uuid

from django.contrib.auth import get_user_model
from django.db import models


class Comment(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField()
    task = models.ForeignKey("front_page.Task", null=True, blank=True, on_delete=models.CASCADE)
    solution = models.ForeignKey("front_page.Solution", null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user} - {self._get_detail}"

    @property
    def _get_detail(self) -> str:
        if self.task or self.solution:
            return f"{self.task or self.solution}"
        return "Invalid comment"

    @property
    def get_reaction(self) -> int:
        from front_page.models import Dislike, Like

        like = Like.objects.filter(comment=self).count()
        dislike = Dislike.objects.filter(comment=self).count()

        return like - dislike

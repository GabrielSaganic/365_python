import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet
from pygments.lexers import get_lexer_by_name
from front_page.models import Comment
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name

class Solution(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    solution = models.TextField()
    task = models.ForeignKey("front_page.Task", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.get_username()} - {self.task.summary}"

    @classmethod
    def get_today_solutions(cls, task):
        return cls.objects.filter(task=task)

    @property
    def get_reaction(self) -> int:
        from front_page.models import Dislike, Like

        like = Like.objects.filter(solution=self).count()
        dislike = Dislike.objects.filter(solution=self).count()

        return like - dislike

    def get_comments(self) -> QuerySet[Comment]:
        return Comment.objects.filter(solution=self).order_by("-created_at")

    @property
    def python_syntax_highlighted_code(self):        
        code = highlight(self.solution, PythonLexer(), HtmlFormatter(style="abap"))
        print(code)
        return code

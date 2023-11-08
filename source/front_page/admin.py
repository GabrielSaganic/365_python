from django.contrib import admin

from front_page import models


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "_get_detail", "created_at", "edited")


@admin.register(models.Dislike)
class DislikeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ("user", "task", "get_reaction", "created_at")


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "summary",
        "date_of_task",
        "get_reaction",
    )

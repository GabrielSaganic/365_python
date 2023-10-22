from datetime import datetime

from django.views.generic import TemplateView

from front_page.models import Task


class TaskDetailView(TemplateView):
    template_name = "front_page/task_detail.html"
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)

        try:
            context["task"] = Task.objects.get(date_of_task=datetime.today())
        except Task.DoesNotExist:
            raise ValueError("Task for today not found!")

        return context
    
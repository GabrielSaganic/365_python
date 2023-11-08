import json

from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from front_page.models import Task, Solution


@method_decorator(csrf_exempt, name="dispatch")
class TaskDetailView(TemplateView):
    template_name = "front_page/task_detail.html"
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)

        try:
            context["task"] = Task.get_today_task()
        except Task.DoesNotExist:
            raise ValueError("Task for today not found!")

        return context
    
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode("utf-8"))
        code = data.get("code", "")
        
        # TODO get logged user
        user = get_user_model().objects.first()
        
        Solution.objects.create(
            user=user,
            task=Task.get_today_task(),
            solution=code,
        )
        from django.http import JsonResponse
        return JsonResponse({"data": "success"}, status=201)

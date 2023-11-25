import json
from typing import Any

from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden

from front_page.models import Task, Solution, Like

@method_decorator(csrf_exempt, name="dispatch")
class SolutionListView(ListView):
    model = Solution
    template_name = "front_page/solution_list.html"
    context_object_name = "solutions"

    def get_queryset(self):
        return Solution.get_today_solutions(Task.get_today_task())
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        user = self.request.user
        if user.is_authenticated:
            context["liked_solution"] = Like.objects.filter(
                user=user,
                solution__task=Task.get_today_task(),
            ).values_list("solution__id", flat=True)

        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("User is not authenticated.")

        data = json.loads(request.body.decode("utf-8"))
        solution_id = data.get("solution_id", "")
        
        user = request.user
        solution = Solution.objects.get(id=solution_id)
        Like.objects.create(
            user=user,
            solution=solution
        )
        
        number_of_like = Like.objects.filter(solution=solution).count()
        
        return JsonResponse({"output": number_of_like}, status=201)


class SolutionDetailView(DetailView):
    model = Solution

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            context["liked_solution"] = Like.objects.filter(
                user=user,
                solution__task=Task.get_today_task(),
            ).values_list("solution__id", flat=True)
        
        return context
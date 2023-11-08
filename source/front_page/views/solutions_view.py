import json

from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from front_page.models import Task, Solution, Like


@method_decorator(csrf_exempt, name="dispatch")
class SolutionListView(ListView):
    model = Solution
    template_name = "front_page/solution_list.html"
    context_object_name = "solutions"

    def get_queryset(self):
        return Solution.get_today_solutions(Task.get_today_task())
    
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode("utf-8"))
        solution_id = data.get("solution_id", "")
        
        # TODO get logged user
        user = get_user_model().objects.first()
        solution = Solution.objects.get(id=solution_id)
        Like.objects.create(
            user=user,
            solution=solution
        )
        
        number_of_like = Like.objects.filter(solution=solution).count()
        
        return JsonResponse({"output": number_of_like}, status=201)
        
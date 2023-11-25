import json

from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, HttpResponse

from front_page.models import Comment, Solution


@method_decorator(csrf_exempt, name="dispatch")
class CommentListView(ListView):       
    def post(self, request, *args, **kwargs):
        user = request.user
        
        if not request.user.is_authenticated:
            return HttpResponseForbidden("User is not authenticated.")
        
        data = json.loads(request.body.decode("utf-8"))
        comment = data.get("comment", "")
        solution_id = data.get("solution_id", "")
        
        comment = Comment.objects.create(
            user=user,
            solution=Solution.objects.get(id=solution_id),
            comment=comment,
        )

        data = {
            "user": comment.user.email,
            "time": comment.created_at.strftime("%b. %d, %Y, %I:%M %p").replace("AM", "a.m.").replace("PM", "p.m.")
        }
        return HttpResponse(data=data, status=201)

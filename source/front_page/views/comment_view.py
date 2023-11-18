from datetime import datetime, timezone
import json

from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from front_page.models import Comment, Solution


@method_decorator(csrf_exempt, name="dispatch")
class CommentListView(ListView):       
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode("utf-8"))
        comment = data.get("comment", "")
        solution_id = data.get("solution_id", "")
        
        # TODO get logged user
        user = get_user_model().objects.first()
        
        comment = Comment.objects.create(
            user=user,
            solution=Solution.objects.get(id=solution_id),
            comment=comment,
        )
        from django.http import JsonResponse
        data = {
            "user": comment.user.email,
            "time": comment.created_at.strftime("%b. %d, %Y, %I:%M %p").replace("AM", "a.m.").replace("PM", "p.m.")
        }
        return JsonResponse(data=data, status=201)

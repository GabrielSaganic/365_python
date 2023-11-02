from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import subprocess
from django.http import JsonResponse
import json

@method_decorator(csrf_exempt, name="dispatch")
class RunCodeView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode("utf-8"))
        code = data.get("code", "")
        
        try:
            result = subprocess.run(
                ["python3", "-c", code],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if result.returncode == 0:
                output = result.stdout
            else:
                output = result.stderr

            return JsonResponse({"output": output})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

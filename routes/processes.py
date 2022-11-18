import seed.routes.processes as SeedRoute
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from seed.util.request_util import has_fields_or_400
from domain.process import create_process

class ProcessViewSet(SeedRoute.ProcessViewSet):
  @action(detail = False, methods = ["POST"])
  def execute(self,request):
    data = request.data
    has_fields_or_400(data, "user_id", "input")
    string_triangle = str(data["input"])        
    user_id = int(data["user_id"])
    min_sum = create_process(string_triangle, user_id)
    return Response(status = status.HTTP_201_CREATED, data = min_sum)
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, Django app!")

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_api(request):
    return Response({"message": "Hello from Django API!"})


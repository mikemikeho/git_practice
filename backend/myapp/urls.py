from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
]

from . views import hello_api
urlpatterns = [
    path('api/hello/', hello_api),
]

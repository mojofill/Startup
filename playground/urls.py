from django.urls import path
from . import views

# URLConf (url configuration)
urlpatterns = [
    path("hello/", views.say_hello)
]

from django.urls import path
from .views import *
urlpatterns = [
    path('hello/',helloview),
    path('emp/',empview)
]
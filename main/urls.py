from django.urls import path
from main.views import *

app_name = "main"

urlpatterns = [
    path('', index, name='index'),
    path('post/', Post, name='post'),
    # path('project/<int:id>/', project, name='project')

]
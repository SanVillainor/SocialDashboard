from django.urls import path
from .views import home,comments,createpost

urlpatterns = [
    path("",home,name='home'),
    path('comments/<str:id>',comments,name="comments"),
    path("createpost/",createpost,name="createpost"),
]
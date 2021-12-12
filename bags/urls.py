from django.urls import path
from .views import *

urlpatterns = [
    path('', Baglist.as_view()),
    path('<int:pk>/', BagDetail.as_view())
]
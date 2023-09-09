from django.urls import path
from API.views import *
urlpatterns =[
    path('',home),
    path('CreateCoder',CreateCoder.as_view(),name="CreateCoder"),
    path('ObtainAuthToken',ObtainAuthTokenView.as_view(),name="ObtainAuthToken"),
    path('ValidateTokien',ValidateTokien.as_view(),name="ValidateTokien")
]
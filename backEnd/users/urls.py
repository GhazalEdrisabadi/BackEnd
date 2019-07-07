from django.urls import path
from .views import *

urlpatterns = [
    path('', UploadDesign.as_view()),
    path('', DesignDetail.as_view())
]
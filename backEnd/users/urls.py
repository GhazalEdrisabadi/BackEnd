from django.urls import path
from .views import *

urlpatterns = [
    path('uploaddesign', UploadDesign.as_view()),
    path('designslist', DesignDetail.as_view()),
]
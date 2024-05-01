from django.urls import path
# from .views import upload_image, upload_video
from .views import home,message
urlpatterns = [
    # path('upload/image/', upload_image, name='upload_image'),
    # path('upload/video/', upload_video, name='upload_video'),
    # add more paths as needed
    path('',home,name="home"),
    path('messages/', message, name='messages'),
]
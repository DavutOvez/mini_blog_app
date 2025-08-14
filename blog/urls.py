from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('post/<int:id>',post_detail,name='post_detail'),
    path('post/new/',post_new,name='post_new'),
    path('post/<int:id>/edit/',post_edit,name='post_edit'),
    path('post/<int:id>/delete/',post_delete,name='post_delete'),
]
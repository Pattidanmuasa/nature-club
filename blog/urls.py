from . import views
from django.urls import path
from blog.views import *


app_name='BLOG'


urlpatterns = [
#     path('', views.PostList.as_view(), name='PostList'),
    # path('',views.PostList.as_view(), name='PostList'),
    path('',views.postlist, name='postlist'),
    path('<str:slug>/', views.PostDetail, name='post_detail'),
]

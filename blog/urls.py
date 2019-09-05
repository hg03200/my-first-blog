from django.urls import path
from . import views

# NoReverseMatch 에러 뜨는 경우!!
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    # post_detail 뷰로 보내 게시글이 보일 수 있게 함
    # <int:pk> : 장고는 정수 값을 기대하고 이를 pk라는 변수로 뷰로 전송
]

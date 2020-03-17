from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # <int:pk>는 조금 까다롭습니다. 장고는 정수 값을 기대하고 이를 pk라는 변수로 뷰로 전송하는 것을 말합니다.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
]
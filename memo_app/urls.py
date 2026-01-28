from django.urls import path
from . import views

urlpatterns = [
    # views.py에 있는 memo_create 함수와 연결합니다.
    path('create/', views.memo_create, name='memo_create'),
]
from django.urls import path
from . import views

# C:\Users\dav00\memo_app\urls.py

urlpatterns = [
    # 기존 주소들
    path('create/', views.memo_create, name='memo_create'),
    path('list/', views.memo_list, name='memo_list'),

    # 가영 님 담당: 상세 페이지 주소 추가 (에러 해결 핵심!)
    path('memo/<int:memo_id>/', views.memo_detail, name='memo_detail'), 
]
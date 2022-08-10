from . import views
from django.urls import path


urlpatterns = [
    path('', views.TopicList.as_view(), name="home"),
    path('<slug:slug>/', views.ThreadDetail.as_view(), name='thread_detail'),
]

# # Code Credit structure to ITTIB by CI, mix of ITTIB and custom
# values for lines 5 to 13


from . import views
from django.urls import path


urlpatterns = [
    path('', views.TopicList.as_view(), name="home"),
    path('<slug:slug>/', views.ThreadList.as_view(), name='thread_list'),
]

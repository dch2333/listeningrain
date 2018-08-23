from django.urls import path
from dachuang import views
urlpatterns = [
    path('', views.dachuang),
    path('random_pic', views.random_pic),
    path('upload_file', views.upload_file),
    path('distinguish_0', views.distinguish_0),
    path('distinguish_1', views.distinguish_1),
    path('introduction', views.introduction),
    path('teacher', views.teacher),
    path('wzy', views.wzy),
    path('dch', views.dch),
    path('pk', views.pk),
    path('login/', views.login),
    path('logout/', views.logout),
]
from django.urls import path, include,re_path
from . import views
from django.views.static import serve
urlpatterns = [
    path('', views.index),
    path('/pic', views.pictures),
    path('/ajax', views.ajax),
    #path('test/', views.test),
    # path('test/<str:num>/', views.test1),
    # path('picture/',views.pics),
    # path('picture/<int:num>/',views.picss),

]
from django.urls import path, include,re_path
from . import views
from django.views.static import serve
urlpatterns = [
    path('', views.index),
    # path('<str:num>/', views.detail),
    #path('test/', views.test),
    path('realtimedate/ajax/', views.ajax),
    path('realtimedate', views.realtimedata),
    path('historydate',views.historydata),
    # path('picture/',views.pics),
    # path('picture/<int:num>/',views.picss),

]

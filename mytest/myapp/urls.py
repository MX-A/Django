from django.urls import path, include,re_path
from . import views
from django.views.static import serve
urlpatterns = [
    path('', views.index),
    path('<str:num>/', views.detail),
    #path('test/', views.test),
    path('test/<str:num>/', views.test1),
    path('ajax/<str:num>', views.ajax),
    #path('mxy/', views.mxy),
    # path('picture/',views.pics),
    # path('picture/<int:num>/',views.picss),

]

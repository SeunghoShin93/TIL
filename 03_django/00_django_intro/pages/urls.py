from django.urls import path
from . import views


urlpatterns = [
    # 원래는 app url 은 아래로 작성해나간다.
    path('index/', views.index),
    path('introduce/<str:name>,<int:age>/', views.introduce),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('template_language/', views.template_language),
    path('hello/<str:name>/', views.hello),
    path('times/<int:a>,<int:b>/', views.times),
    path('area/<int:r>/', views.area),
    path('throw/', views.throw),
    path('isitgwangbok/', views.isitgwangbok),
    path('catch/', views.catch),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]
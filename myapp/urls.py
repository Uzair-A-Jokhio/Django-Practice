from django.urls import path
from . import views

urlpatterns = [
    
    # path('say_hello/', views.say_hello, name="say_hello"),
    path('', views.homepage, name='home_page'),
    path('display_date/', views.display_date, name='display_date'),
    path('info/', views.info, name='info'),
    # path('names/<str:name>/<int:id>' ,views.getname, name='names'),
    path('showform/', views.showform, name='showform'),
    path('getform/', views.getform, name="getforms"),


    path('forms/', views.index, name="forms" ),
    path('details/', views.details_of_user, name='details'),
    path('home/', views.home, name='home')

]
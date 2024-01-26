from django.urls import path
from . import views

urlpatterns = [
    path('menuitem/', views.menu_items),
    path('menuitem/<int:id>', views.single_item),
]




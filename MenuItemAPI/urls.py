from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('menuitem/', views.menu_items),
    path('menuitem/<int:id>', views.single_item),

    path('category', views.CategoriesView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('secret_msg/' , views.some_secret),
    path('api-token-auth/', obtain_auth_token)
]
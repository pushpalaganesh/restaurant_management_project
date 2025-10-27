from django.urls import path
from .views import home,MenuCategoryListView

urlpatterns = [
    path('', home, name = 'home'), # url path of homepage
    path('menu-categories/', MenuCategoryListView.as_view(), name='menu-category-list'),
]
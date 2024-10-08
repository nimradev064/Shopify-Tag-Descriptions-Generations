from django.urls import path
from .views import product_list, get_all_tags

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('all-tags/', get_all_tags, name='all-tags'),
]

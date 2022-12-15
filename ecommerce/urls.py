from django.urls import path, re_path
from . import views
app_name = 'shop'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    re_path(r'detail_list/(?P<category_slug>[-\w]+)/', views.product_list, name='product_list_by_category'),
    re_path(r'detail/(?P<id>[-\w]+)/(?P<slug>[-\w]+)/', views.product_detail, name='product_detail'),
]

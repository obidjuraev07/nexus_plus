from django.urls import path
from .views import home, details, post_ad, products
urlpatterns = [
    path('', home, name='home'),
    path('details/<slug:slug>/', details, name='details'),
    path('post/', post_ad, name='post_ad'),
    path('products/', products, name='products'),
    path('category/<slug:ctg_slug>/', products, name='category')
]

from django.urls import path
from .views import blog, add_post, add_db, blog_detail, search

urlpatterns = [
    path('blog_content/', blog, name='blog'),
    path('add_post/', add_post, name='add_post'),
    path('add_blog/', add_db, name ='add_blog'),
    path('blog_content/<int:id>', blog_detail, name ='commet'),
    path('blog_content/searching', search, name='search')
]



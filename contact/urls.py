from django.urls import path, include
from .views import contact,page_404,page_faq,page_about,page_pricing,page_services
urlpatterns = [
    path('', contact, name='contact'),
    path('page_404', page_404, name='page_404'),
    path('page_faq', page_faq, name='page_faq'),
    path('page_about', page_about, name='page_about'),
    path('page_services', page_services, name='page_services'),
    path('page_pricing', page_pricing, name='page_pricing'),
]

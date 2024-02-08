
from django.urls import path
from . import views

urlpatterns = [
    path('admin-login/', views.admin_login, name='admin_login'),
    path('property-listing/', views.property_listing, name='property_listing'),
    path('property-profile/<int:property_id>/', views.property_profile, name='property_profile'),
    path('tenant-profile/<int:tenant_id>/', views.tenant_profile, name='tenant_profile'),
    path('property-search/', views.property_search, name='property_search'),
]

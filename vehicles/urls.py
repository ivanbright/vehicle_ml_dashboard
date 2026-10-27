# vehicles/urls.py
from django.urls import path
from .views import dashboard_view, price_filter_view, group_view

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
    path("price-filter/", price_filter_view, name="price_filter"),
    path("group-view/",  group_view, name="group_view"),
]

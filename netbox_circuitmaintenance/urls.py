from django.urls import path, include

from netbox.views.generic import ObjectChangeLogView
from . import models, views
from utilities.urls import get_model_urls

app_name = "netbox_circuitmaintenance"

urlpatterns = (
    path(
        "circuitmaintenance/",
        include(get_model_urls("netbox_circuitmaintenance", "circuitmaintenance", detail=False)),
    ),
    path(
        "circuitmaintenance/<int:pk>/",
        include(get_model_urls("netbox_circuitmaintenance", "circuitmaintenance")),
    ),
    path(
        "circuitimpact/",
        include(get_model_urls("netbox_circuitmaintenance", "circuitmaintenanceimpact", detail=False)),
    ),
    path(
        "circuitimpact/<int:pk>/",
        include(get_model_urls("netbox_circuitmaintenance", "circuitmaintenanceimpact")),
    ),
    path(
        "circuitnotification/",
        include(get_model_urls("netbox_circuitmaintenance", "circuitmaintenancenotifications", detail=False)),
    ),
    path(
        "circuitnotification/<int:pk>/",
        include(get_model_urls("netbox_circuitmaintenance", "circuitmaintenancenotifications")),
    ),
    path('maintenanceschedule/', views.CircuitMaintenanceScheduleView.as_view(), name='maintenanceschedule'),
)

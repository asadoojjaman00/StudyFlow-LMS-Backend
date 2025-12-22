

from django.urls import path
from modules.views.moduleviews import (
    ModuleCreateView,
    ModuleUpdateView,
    ModuleDeleteView
)

urlpatterns = [
    path("module/create/",ModuleCreateView.as_view(),name="module-create"),

    path("module/<int:id>/update/",ModuleUpdateView.as_view(),name="module-update"),

    path("module/<int:id>/delete/",ModuleDeleteView.as_view(),name="module-delete"),
]

from django.urls import path
from . import views

urlpatterns =[
    # path("january", views.january),
    # path("february", views.february),
    path("", views.index),
    path("<int:id>",views.month_by_number),
    path("<str:id>",views.month, name="month-name"),
]
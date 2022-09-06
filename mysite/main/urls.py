from django.urls import path

from .import views

urlpatterns = [
    path("<str:name>", views.list, name="list"),
    path("kale/", views.kale, name="page 1"),
    path("", views.index, name ="index")
]

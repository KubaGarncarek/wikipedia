from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.greet, name="greet"),
    path("search", views.search, name="search"),
    path("new_page", views.new_page, name="new_page"),
]

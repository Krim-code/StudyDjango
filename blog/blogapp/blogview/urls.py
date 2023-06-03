from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="posts"),
    path("post/create", views.create_form,name='post-create'),
    path("about/",views.about,name="about")
]

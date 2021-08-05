from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.create_user),
    path('success', views.success),
    path("show", views.show)
]
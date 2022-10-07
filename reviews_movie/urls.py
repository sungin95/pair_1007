from django.urls import path
from . import views

app_name = "review"

urlpatterns = [
    path("", views.main, name="main"),
    path("index/", views.index, name="index"),
    path("new/", views.new, name="new"),
    path('detail/<int:pk>',views.detail, name='detail'),
    path('detail/<int:pk>/update',views.update, name='update'),
    path('detail/<int:pk>/delete',views.delete, name='delete'),
    path("aadmin/", views.admin, name='aadmin'),
    path("aadmin/create", views.admin_create),
]

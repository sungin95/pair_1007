from django.urls import path
from . import views

app_name = "review"

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('detail/<int:pk>/update',views.update,name='update'),
    # path('detail/<int:pk>/delete',views.delete,name='delete'),

   
]

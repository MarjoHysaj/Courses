from django.urls import path     
from . import views

urlpatterns = [
    path('courses', views.index),
    path('courses/create', views.create),
    path('courses/<int:id>', views.show),
    path('courses/<int:id>/edit', views.edit),
    path('courses/<int:id>/destroy', views.destroy),
    path('courses/comment/<int:id>', views.commentshow),
    path('courses/comment/<int:id>/create', views.commentcreate),
]
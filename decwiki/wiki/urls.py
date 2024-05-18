from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_content_view, name='create_content'),
    path('content/<int:content_id>/', views.content_detail, name='content_detail'),
    path('content/<int:content_id>/upvote/', views.upvote_content_view, name='upvote_content'),
    path('content/<int:content_id>/downvote/', views.downvote_content_view, name='downvote_content'),
]
from . import views
from django.urls import path

urlpatterns = [
    path("", views.MovieListView.as_view(), name="home"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path(
        '<slug:slug>/edit_comment/<int:comment_id>/',
        views.comment_edit,
        name='comment_edit'),
    path(
        '<slug:slug>/delete_comment/<int:comment_id>/',
        views.comment_delete,
        name='comment_delete'),
    path('approve_comment/<int:comment_id>/', views.approve_comment,
         name='approve_comment'),
]

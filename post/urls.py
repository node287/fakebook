from django.urls import path
import post.views

urlpatterns = [
    path('', post.views.home, name='home'),
    path('create/', post.views.create, name='create'),
    path('<int:post_id>/', post.views.details, name='details'),
    path('<int:post_id>/like_post', post.views.like_post, name="like_post"),
    path('<int:post_id>/dislike_post', post.views.dislike_post, name="dislike_post"),

]

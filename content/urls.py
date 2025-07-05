#imports
from django.urls import path
from content import views

#--------------------------------------------------------------------------------------------------
#Path
urlpatterns = [
    path("api/register/", views.register_user),
    path("api/login/", views.login_user),
    path("api/create-post/", views.create_post),
    path("api/posts/", views.get_all_posts),
    path("api/post/<int:id>/", views.get_post_detail),
    path("api/post/<int:id>/comment/", views.add_comment),
]

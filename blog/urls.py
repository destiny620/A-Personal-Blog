from django.urls import path
from . import views
from .views import blogsView, AddBlogPostView, AddProfileView, EditBlogPostView, DeleteBlogPostView, EditProfileView, DeleteProfileView
                    

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", blogsView.as_view(), name="blogsView"),
    path('blog/', views.blog, name='blog'),
    path("blog_detail/<str:slug>/", views.Blog_Detail, name="blog_detail"),
    path('profile/', views.profile, name='profile'),
    path("add_blogpost/", AddBlogPostView.as_view(), name="add_blogpost"),
    path("add_profile/", AddProfileView.as_view(), name="add_profile"),
    path("edit_blogpost/<str:slug>/", EditBlogPostView.as_view(), name="edit_blogpost"),
    path("delete_blogpost/<str:slug>/", DeleteBlogPostView.as_view(), name="delete_blogpost"),
    path('profile/edit/', EditProfileView.as_view(), name='profile/edit'),
    # path("edit_profile/", EditProfileView.as_view(), name="edit_profile"),
    path("delete_profile/<str:pk>/", DeleteProfileView.as_view(), name="delete_profile"),
    # path('user_profile/<str:pk>/', views.User_Profile, name='user_profile'),
    # path('edit_profile/', views.edit_profile, name='edit_profile'),
    # path('edit_profile/', views.edit_profile, name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

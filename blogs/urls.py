from django.urls import path
from django.contrib.auth import views as auth_views

from .views import home,checkbtn, subscribeView,replaycommentview,previewBlogsView,homepage,LikeView,blogsettingsview ,AddPostView,searchview,contactlistView,taggedview,BlogCommentView,EditPostView, DeletePosttView, HomeView,FQView ,AddCategoryView,BlogsView, ContactView,AboutView
urlpatterns = [
    path('blog/<int:pk>/<slug:preview>',home,name="blog"),
        path('blog/<int:pk>',home,name="blog"),

    path('',homepage,name='blog'),

    path('index',HomeView,name="home"),


    path("like/<int:pk>", LikeView, name="like_post"),


    path("add_post/",AddPostView.as_view(),name='add_post'),
    path("edit/<int:pk>",EditPostView.as_view(),name='edit_post'),
    path('remove/<int:pk>/',DeletePosttView.as_view(),name="delete_post"),
    path("addCategory",AddCategoryView.as_view(),name="add_category"),
    path("blogs/",BlogsView,name="blogs"),
    path("contact/",ContactView,name="contact"),
    path('about/',AboutView,name='about'),
    path('f&q/',FQView,name='f&q'),
    path('blog/comment',BlogCommentView,name='add_comment'),

    path('replay/',replaycommentview,name='replaycomment'),

    path('tagged/<slug:slug>',taggedview,name='tagged'),
    path('search/',searchview,name='search'),
    path('contact-list',contactlistView,name="contact-list"),
    path('blog-settings',blogsettingsview,name='blog-settings'),
    path('checkbtn/<int:pk>',checkbtn,name='checkbtn'),
        path("blogs/<int:pk>",previewBlogsView,name="previewblogs"),
        path('subscribe/',subscribeView,name="subscribe")



]

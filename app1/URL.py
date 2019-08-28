from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index , name='index' ),
    url(r'^login/' ,views.login , name='login' ),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^dashbord/',views.dashbord, name='dashbord'),
    url(r'^product/', views.product, name='product'),
    url(r'^create/', views.book_create_1, name='create' ),
    url(r'^create_pen/', views.pen_create_1, name='create' ),
    url(r'^add_book/', views.add_book_1, name='add_book' ),
    url(r'^delete/(?P<id>\d+)/', views.delete_book_1, name='delete' ),
    url(r'^delete_pen/(?P<id>\d+)',views.delete_pen_1 , name='delete_pen'),
    url(r'^edit/(?P<id>\d+)/', views.edit_book_1, name='edit' ),
    url(r'^edit_pen/(?P<id>\d+)/', views.edit_pen_1, name='edit_pen' ),
    url(r'^update/(?P<id>\d+)/', views.update_book_1, name='update' ),
    url(r'^update_pen/(?P<id>\d+)/', views.update_pen_1, name='update_pen' ),
    url(r'^index/',views.hello, name='hello'),
    url(r'^pen/', views.penlist, name='pen'),
    url(r'^add_pen/', views.add_pen_1, name='add_pen'),
    url(r'^blog_admin/', views.blog_admin, name='blog_admin'),
    url(r'blog_post/',views.blog_post , name='blog_post'),
    url(r'^create_post/', views.create_post, name='create_post' ),
    url(r'^see_post/', views.see_post, name ='see_post'),
    url(r'^edit_blog/(?P<id>\d+)/', views.edit_blog, name='edit_blog' ),
    url(r'^update_blog/(?P<id>\d+)/', views.update_blog, name='update_blog'),
    url(r'^delete_blog/(?P<id>\d+)',views.delete_blog , name='delete_blog'),

]
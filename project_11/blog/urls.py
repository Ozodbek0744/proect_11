from django.urls import path
from .views import blog_list_view, blog_post, blog_detail_view, post_comment, comment_list_view, \
    update_comment_post, delete_comment, author_list_view,\
    update_delete_blog_post, author_list_comment, comment_izoh

app_name = 'blog'

urlpatterns = [
    path('post', blog_post),
    path('list', blog_list_view),
    path('list/<slug:slug>', blog_detail_view),
    path('update_delete_blog_post/<slug:slug>',update_delete_blog_post),
    path('comment/<int:pk>', post_comment),
    path('comment/list', comment_list_view),
    path('comment/update/<int:pk>', update_comment_post),
    path('comment/delete/<int:pk>', delete_comment),
    path('author_post', author_list_view),
    path('author_comment', author_list_comment),
    path('commment_izoh/<int:pk>', comment_izoh)
]




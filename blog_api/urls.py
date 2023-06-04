from django.urls import path
from .views import PostDetail, PostList, PostListDetailFilter
# from rest_framework.routers import DefaultRouter



app_name = 'blog_api'

""" 
router = DefaultRouter()
router.register('', PostDetail, basename='post')
urlpatterns = router.urls
 """


urlpatterns = [
    path('<str:pk>/', PostDetail.as_view(), name= 'detailcreate'),
    path('search/', PostListDetailFilter.as_view(), name= 'postsearch'),
    path('', PostList.as_view(), name='listcreate'),
]



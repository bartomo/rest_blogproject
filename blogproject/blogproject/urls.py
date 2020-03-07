from django.contrib import admin
# from django.urls import path
from django.conf.urls import url, include
from blogapp import views
from blogapp.urls import router

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^post/', views.index, name='index'),
    url(r'^result/', views.post_result, name='post_result'),
    url(r'^user/', views.UserViewSet, name='user'),
    url(r'^search/', views.search, name='search'),
    url(r'^extends/',views.base_test, name='base_test'),
    url(r'', views.timeline, name='timeline'),
    ]
    

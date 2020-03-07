from django.contrib import admin
from django.urls import path,include
from . import views
import blogproject
from rest_framework import routers

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'', include('blogproject.urls'))
]

router = routers.DefaultRouter()
router.register(r'entry', views.EntryViewSet)
router.register(r'user', views.UserViewSet)
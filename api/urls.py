from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from api.views import PostViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'post', PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]

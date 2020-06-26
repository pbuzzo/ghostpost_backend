from django.conf.urls import include, url
from api.views import PostViewSet, RoastViewSet, BoastViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'roasts', RoastViewSet, basename='roasts')
router.register(r'boasts', BoastViewSet, basename='boasts')

urlpatterns = [
    url(r'^api/', include(router.urls))
]

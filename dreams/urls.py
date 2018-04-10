from django.conf.urls import url
from rest_framework import routers
from dreams.views import DreamViewSet

router = routers.DefaultRouter()
router.register(r'dreams', DreamViewSet)

urlpatterns = router.urls
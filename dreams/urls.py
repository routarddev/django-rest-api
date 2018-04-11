from django.conf.urls import url, include
from rest_framework import routers
from dreams.views import DreamViewSet

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Dreams API')

router = routers.DefaultRouter()
router.register(r'dreams', DreamViewSet)

urlpatterns = [
    #url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^docs/', schema_view),
]
urlpatterns += router.urls
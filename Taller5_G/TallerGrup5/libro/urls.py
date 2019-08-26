from rest_framework import routers
from django.conf.urls import url
from .views import *

from .viewsets import *

router = routers.SimpleRouter()

router.register('user', UserViewSet)
router.register('autor', AutorViewSet)
router.register('libro', LibroViewSet)
router.register('persona', PersonaViewSet)
router.register('rate', RateViewSet)
router.register('autor_libro', AutorLibroViewSet)

urlpatterns = router.urls


# urlpatterns = [

# 	url(regex=r'^hello/',view=hello_world,name='hello_world'),
# 	url(regex=r'^autores/',view=list_autores,name='list'),
# ]




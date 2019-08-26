from rest_framework import routers

from .viewsets import *

router = routers.SimpleRouter()

router.register('user', UserViewSet)
router.register('autor', AutorViewSet)
router.register('libro', LibroViewSet)
router.register('persona', PersonaViewSet)
router.register('rate', RateViewSet)
router.register('autor_libro', AutorLibroViewSet)

urlpatterns = router.urls

from django.conf.urls import url
from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from .views import librosViewSet


merouter = merouters.DefaultRouter()
merouter.register(r'libros', librosViewSet)

urlpatterns = [

]

urlpatterns += merouter.urls
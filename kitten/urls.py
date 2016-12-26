from django.conf.urls  import url
from . import views

urlpatterns = [
    url(r'^$', views.kitten_home, name='kitten_home'),
]

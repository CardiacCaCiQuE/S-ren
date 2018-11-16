from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.PerroView.as_view()),
    url(r'^filtro/(?P<filtro>[a-zA-Z]+)$',views.PerroFiltro.as_view()),
    url(r'^add/$',views.PerroFiltro.as_view()),
]
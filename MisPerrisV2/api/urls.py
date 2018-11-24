from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^perro$',views.PerroView.as_view()),
]

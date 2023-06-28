from django.urls import path,include
from . import views

urlpatterns=[
    path("",views.shortener,name="shortener"),
    path("s/<str:slug>",views.urlRedirect,name="redirect"),
    path("",include("registration.urls")),
]
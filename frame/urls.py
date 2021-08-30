from django.urls import path

from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("elements", views.elements, name="elements" ),
    path("eventsnews", views.eventsnews, name="eventsnews"),
    path('events', views.events, name="events"),
    path("qwer", views.qwer, name="qwer"),
    path("single-event", views.singleevent, name="single-event")
]
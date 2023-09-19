from django.urls import path
from .views import *

urlpatterns=[
    path('',index),
    path('log/',log),
    path('reg/',reg),
    path('edit/<int:id>',edit),
    path('login/',login),
    path('register/',register),
    path('stu/<int:id>',stu),
    path('asgmnt/<int:id>',asgmnt),
    path('stuasg/<int:id>',stuasg),
    path('subasg/<int:id1>/<int:id2>',subasg),
    path('viewasg/<int:id>',viewasg),
    path('sbjtasg/<int:id>',sbjtasg),
    path('review/<int:id>',review),
    path('rev/<int:id>',rev),
    path('re/<int:id>',re),
    path('pnotes/<int:id>',pnotes),
    path('note/<int:id>',note),
]
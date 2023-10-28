from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.rep_post,name='rep_post')
]

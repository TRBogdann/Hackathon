from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.rep_post,name='rep_post'),
    path('login/',views.log_usr,name='log_usr'),
    path('locatie/',views.view_app,name='view_app'),
    path('creare/',views.user_post,name='user_post'),
    path('finalizare/',views.view_finalizare,name='view_finalizare')
]

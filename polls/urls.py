"""
    `urls.py`
    Contains URLs in `polls` application
"""

from django.urls import path

from polls import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/<int:poll_id>/', views.detail, name='detail'),
    path('detail/<int:poll_id>/comment/', views.comment, name='comment'),
    path('create/', views.create, name='create'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('update/<int:poll_id>/', views.update, name='update_poll'),
]

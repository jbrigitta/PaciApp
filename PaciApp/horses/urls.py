from django.urls import path

from horses import views

app_name = 'horses'

urlpatterns = [
    path('game/', views.game, name='game')
]

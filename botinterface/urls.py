from django.urls import path
from . import views

app_name = 'botinterface'
urlpatterns = [
    path('comment/<int:site>/', views.comments, name='comments'),
    path("message/8123", views.test)
]

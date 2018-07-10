from django.urls import path
from . import views
from .tokens import WEB_TOKEN
app_name = 'botinterface'
urlpatterns = [
    path('comment/<int:site>/', views.comments, name='comments'),
    path("message/" + WEB_TOKEN, views.test)
]

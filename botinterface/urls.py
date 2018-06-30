from django.urls import path
from . import views

app_name = 'botinterface'
urlpatterns = [
    path('<int:site>/', views.comments, name='comments'),
    path("test/", views.test)
]

from django.urls import path
from . import views

app_name = 'botinterface'
urlpatterns = [
    path('<int:site_id>', views.comments, name='comments')
]

from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.main, name = 'main'),
    path('tag/', views.tag,  name = 'tag'),
    path('quote/', views.quote, name='quote'),
    path('author/', views.author, name='author'),
    path('detail/<int:quote_id>', views.quote_info, name='quote_info'),
    path('detail/<str:author_name>', views.about_author, name='about_author'),
]

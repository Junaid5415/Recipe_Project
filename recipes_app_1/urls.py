from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('', views.index, name='index'),
     path('table/', views.table, name='table'),
     path('delete_recipe/<id>/', views.delete_recipe, name='delete_recipe'),
     path('edit_recipe/<id>/', views.edit_recipe, name='edit_recipe')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
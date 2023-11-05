from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('listaPosts', views.listaPosts, name="listaPosts"),
    path('detalhePost/<int:id>/', views.detalhePost, name='detalhePost')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
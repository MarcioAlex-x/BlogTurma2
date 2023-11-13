from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('listaPosts', views.listaPosts, name="listaPosts"),
    path('detalhePost/<int:id>/', views.detalhePost, name='detalhePost'),
    path('login',views.login_view,name='login'),
    path('logout/', views.logout_view, name='logout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
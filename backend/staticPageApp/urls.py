from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from staticPageApp.views import StaticPage, MainPage


urlpatterns = [
    path('<slug:slug_page>/', StaticPage.as_view(), name='static-page'),
    path('', MainPage.as_view(), name='main'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from projectApp.views import ListProject, PageProject


urlpatterns = [
    path('<slug:slug_project>/', PageProject.as_view(), name='page-project'),
    path('', ListProject.as_view(), name='main-project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
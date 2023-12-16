from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = staticfiles_urlpatterns()

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path("poets", views.poets, name="poets"),
    path('about', views.about, name="about"),
    path("quotes", views.quotes, name="quotes"),
    path("contacts", views.contacts, name="contacts"),
    path("videos", views.videos, name="videos"),
    path('blogs', views.BlogList.as_view(), name='blogs'),
    path('<slug:slug>/', views.Detail.as_view(), name='details'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


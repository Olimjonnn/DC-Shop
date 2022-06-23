from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/<int:pk>/', ProductPk.as_view()),
    path('contact/', ContactView.as_view()),
    path('productt/', ProductView.as_view()),
    path('review/', ReviewVw.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

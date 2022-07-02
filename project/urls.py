"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('errors.urls', namespace='errors_app')),
    path('register/', include('register.urls', namespace='register_app')),
    path('dashboard', include('dashboard.urls', namespace='dashboard_app')),
    path('dashboard/message_engine', include('message_engine.urls', namespace='message_engine_app')),
    path('offers', include('offers.urls', namespace='offers_app')),
    path('', include('selenium_conf.urls', namespace='selenium_conf_app')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'errors.views.page_not_found_view'
handler500 = 'errors.views.error_view'
handler403 = 'errors.views.permission_denied_view'
handler400 = 'errors.views.ad_request_view'
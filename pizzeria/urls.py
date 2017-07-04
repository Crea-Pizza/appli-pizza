"""pizzeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views import static

from app.views.index import IndexView
from app.views.json.connected import JsonIsConnectedView
from app.views.json.login import JsonLoginView
from app.views.json.logout import JsonLogout
from app.views.register import RegisterView
from pizzeria import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='app_index'),
    url(r'^login/$', JsonLoginView.as_view(), name='app_json_login'),
    url(r'^logout/$', JsonLogout.as_view(), name='app_json_logout'),
    url(r'^json/connected/$', JsonIsConnectedView.as_view(), name='app_connected'),
    url(r'^register/$', RegisterView.as_view(), name='app_register'),
    url(r'^public/(?P<path>.*)$', static.serve, {
        'document_root': settings.MEDIA_ROOT
    }, name='url_public'),
]
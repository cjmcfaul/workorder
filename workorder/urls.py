"""workorder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from Order import views
from django.views.generic import TemplateView, RedirectView

urlpatterns = [

    url(r'^workorder/(?P<workorder_id>[0-9]+)/edit_wo/$',
        views.edit_wo, name='edit_wo'),

    url(r'^admin/', admin.site.urls),

    url(r'^workorder/create_wo/$',
        views.create_wo, name='create_wo'),

    url(r'^workorder/(?P<workorder_id>[0-9]+)/$',
        views.workorder, name='workorder'),

    url(r'^$', views.index, name='home'),
]

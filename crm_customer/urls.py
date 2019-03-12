"""crm_customer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include, re_path
from django.contrib import admin
from stark.service.v1 import site
from crm.views import account
from django.views.static import serve
from crm_customer import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stark/', site.urls),
    url(r'^rbac/', include('rbac.urls', namespace='rbac')),
    url(r'^login/', account.login, name='login'),
    url(r'^logout/', account.logout, name='logout'),
    url(r'^index/', account.index, name='index'),
    re_path(r"media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),

]

"""firstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path, include,reverse
from learn import views as learn_views
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # path('', learn_views.firstView),,
    # path('add1/', learn_views.add1, name='add1'),
    # path('add2/<int:a>/<int:b>/', learn_views.add2, name='add2'),
    # path('', learn_views.index,name='home'),
    # re_path(r'^new_add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),
    # path('learn/',include(('learn.urls',"learn"), namespace='nmesp')),
    # path('', learn_views.home, name="home"),  # new
]

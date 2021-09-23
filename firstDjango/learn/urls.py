from django.contrib import admin
from django.urls import path,re_path,include
from learn import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('app1/',views.firstView),
    # path('', learn_views.firstView),
    # path('add1/', learn_views.add1, name='add1'),
    path('add2/<int:a>/<int:b>/', views.add2, name='add2'),
    # path('', learn_views.index,name='home'),
    #
    # re_path(r'^new_add/(\d+)/(\d+)/$', learn_views.add2, name='add2')
    ]
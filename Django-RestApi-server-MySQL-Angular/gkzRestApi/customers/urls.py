from django.conf.urls import url
from customers import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    url(r'^customers/$', views.customer_list),
    url(r'^customers/(?P<pk>[0-9]+)$', views.customer_detail),
    url(r'^customers/age/(?P<age>[0-9]+)/$', views.customer_list_age),
    # path('', include('users.urls')),
    path('admin/', admin.site.urls),
]

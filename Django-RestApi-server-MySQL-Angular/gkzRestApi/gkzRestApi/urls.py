from django.conf.urls import url, include
from django.urls import path
from customers import views

urlpatterns = [
    url(r'^', include('customers.urls')),
    # path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),

]

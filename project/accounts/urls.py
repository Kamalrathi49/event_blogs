from django.urls import path
from django.conf.urls import url
from accounts import views

app_name = 'accounts'
urlpatterns = [
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
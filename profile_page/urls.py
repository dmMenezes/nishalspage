from django.conf.urls import url
from . import views

urlpatterns=[
    url('',views.profile_view,name="profile")
]
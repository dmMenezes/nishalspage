from django.conf.urls import url
from . import views

app_name="upload"

urlpatterns=[
    url('',views.button_upload,name="button_upload"),
    url('upload_form/',views.upload_form,name="upload_form")
]
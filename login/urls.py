from django.conf.urls import url
from login import views

urlpatterns = [
    url(r'^test/', views.test),
    url(r'^index/',views.index)
]

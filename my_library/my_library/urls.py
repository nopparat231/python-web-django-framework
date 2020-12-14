from django.conf.urls import url
from book_management import views

urlpatterns = [
    url(r'^my_index/$', views.index)
]
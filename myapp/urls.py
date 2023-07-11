from django.contrib import admin
from django.urls import path
from myapp import views
admin.site.site_header = "Krushna Django "
admin.site.site_title = " Learning Django "
admin.site.index_title = "Welcome to Django by Krushna "
urlpatterns = [
   path("" , views.index , name='myapp'),
   path("index", views.index, name='Home'),
   path("facebook" , views.facebook , name='facebook'),
   path("contact" , views.contact , name='contact '),
   path("services" , views.services , name='services')

]

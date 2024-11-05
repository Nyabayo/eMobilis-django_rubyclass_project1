from django.urls import path

from myapp import views
from myapp.views import about

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),

]


from django.urls import path
from . import views


urlpatterns = [
      path('', views.index, name='index'),
      path('about/',views.about,name='about'),
      path('facilities/',views.facilities,name='facilities'),
      path('gallery/',views.gallery,name='gallery'),
      path('treatment/',views.treatment,name='treatment'),
      path('advtreatment/',views.advtreatment,name='advtreatment'),

]
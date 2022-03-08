from django.urls import path
from api import views
from django.views.generic import TemplateView

urlpatterns=[

    path('getGenderRatio',views.Resources.as_view()),
    path('senates/list',views.senatelist.as_view()),
    path('senate', views.senate.as_view()),
]
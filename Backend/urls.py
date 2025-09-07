from django.urls import path
from backendApp import views
urlpatterns = [
    path('indexpage/',views.indexpage,name="indexpage")
]
from django.urls import path, include
from . import views
from rest_framework import routers
from .views import *

route = routers.DefaultRouter()
route.register("home", DataListView, basename="home")
route.register("search_filter", SearchRecordView, basename="search_filter")

urlpatterns = [
     path("", include(route.urls)),
     path('register/', RegisterView.as_view(), name="register"),
     path('admin_login/', CustomAuthToken.as_view(), name="admin_login"),
     path('search_input/', SearchRecordInput.as_view(), name="search_input"),
    # path('home/', DataListView.as_view(), name='home'),
    # path('result/', AjaxHandlerView.as_view(), name='result'),

]
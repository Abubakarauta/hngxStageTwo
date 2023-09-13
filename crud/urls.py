from django.urls import path
from .views import PersonDetail,PersonList
urlpatterns = [
    path('api/', PersonList.as_view(), name= 'person-list'),
    path('api/<int:pk>/',PersonDetail.as_view(), name = 'person-detail'),
]
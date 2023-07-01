from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index , name="index"),
    path('notes/', views.getNotes , name="notes"),
   path("notes/<str:pk>/",views.getNote,name="getNote"),
   path("notes/<str:pk>/update",views.updateNote,name="updateNote"),
   path("notes/<str:pk>/delete",views.deleteNote,name="deleteNote"),
   path("notes/create",views.createNote,name="createNote")
    

]
from django.urls import path

from todo2app import views

urlpatterns = [

path('',views.home,name="home"),
path('details/<int:id>',views.details,name="details"),
path('delete/<int:taskid>',views.delete,name="delete"),
path('update/<int:id>',views.update,name="update"),
path('Cbvlist',views.Cbvlist.as_view(),name="Cbvlist"),

path('Cbvdetails/<int:pk>',views.Cbvdetails.as_view(),name="Cbvdetails"),
path('Cbvupdate/<int:pk>',views.Cbvupdate.as_view(),name="Cbvupdate"),

path('Cbvdelete/<int:pk>',views.Cbvdelete.as_view(),name="Cbvdelete"),
]
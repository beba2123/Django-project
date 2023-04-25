from django.urls import path
from . import views
urlpatterns=[
    path('',views.projects,name="projects"),
    path('project/<str:pk>',views.project,name="project"),
    path('create-project/',views.createProject,name='create-project'),
    path('update-project/<str:pk>/',views.updateproject,name='update-project'),
    path('delete-project/<int:pk>/', views.deleteProject,name='delete-project')
] 
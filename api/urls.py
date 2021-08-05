from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('task-list/', views.taskList, name="task-list"),
	path('task-create/', views.taskCreate, name="task-create"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]

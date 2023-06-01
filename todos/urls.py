from django.urls import path

from . import views

urlpatterns = [
	path('', views.todo_view, name="todo"),
	path('delete/<int:id>/', views.todo_delete, name="delete"),
	path('update-todo/<int:id>', views.update_todo, name='update-todo'),
	path('logout/', views.logout_view, name="logout"),

]
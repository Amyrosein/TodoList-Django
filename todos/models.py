from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"Todo number {self.id}"

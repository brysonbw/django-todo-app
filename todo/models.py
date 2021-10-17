from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField()

    # Return String representation of the model
    # It will return the 'Todo'
    def __str__(self):
        return self.name

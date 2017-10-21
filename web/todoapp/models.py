from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField("Nme", max_length=50)
    done = models.BooleanField("IsDone")
    created_at = models.DateTimeField("CreatedDate", auto_now_add=True)

    def __str__(self):
        return self.name
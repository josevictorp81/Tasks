from django.db import models

class Task(models.Model):
    STATUS = (
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    )

    title = models.CharField(max_length=150)
    description = models.TextField()
    done = models.CharField(max_length=5, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

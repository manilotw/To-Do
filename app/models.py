from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)


    def __str__(self):
        return self.title
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    CATEGORY_CHOICES = [
        ('work', 'Работа'),
        ('education', 'Образование'),
        ('other', 'Другое'),
    ]
    is_quickly = models.BooleanField(default=False)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='other'
    )

    def __str__(self):
        return self.title
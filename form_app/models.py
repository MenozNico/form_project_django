from django.db import models

class Message(models.Model):
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    object = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.object


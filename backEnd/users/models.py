from django.db import models

class Design(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

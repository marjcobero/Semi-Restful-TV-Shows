from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be 5 characters long."
        if len(postData['network']) < 3:
            errors['network'] = "Network must be 3 characters long."
        if len(postData['description']) < 10:
            errors['description'] = "Description must be 10 characters long."
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ShowManager()
    
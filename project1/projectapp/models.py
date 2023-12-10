from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.username                                   

class FeedbackProvider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    is_anonymous = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'feedback_provider'

class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_name = models.TextField()

    class Meta:
        db_table = 'building'

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.TextField()
    building= models.ForeignKey(Building, on_delete=models.CASCADE)

    class Meta:
        db_table = 'category'


class FeedbackEntry(models.Model):
    feedback = models.AutoField(primary_key=True)
    provider = models.ForeignKey(FeedbackProvider, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_image = models.ImageField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'feedback_entry'

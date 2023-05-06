from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    email = models.EmailField(blank=False)
    height = models.FloatField()
    weight = models.FloatField()
    target_weight = models.FloatField()

    REQUIRED_FIELDS = ["email", "height", "weight","target_weight"]

    def __str__(self):
        return self.username
    
    def reach_target(self):
        if self.weight > self.target_weight:
            return self.weight - self.target_weight
        
        elif self.weight < self.target_weight:
            return self.target_weight - self.weight

    def get_bmi(self):
        return self.weight / ((self.height / 100) * (self.height / 100))
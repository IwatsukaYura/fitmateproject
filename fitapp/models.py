from django.db import models
from django.contrib.auth.models import AbstractUser

AGECHOICE = (('young','10~20'),('youngn adult','20~30'),('adult','30~40'),('senior','40~50'))

class CustomUser(AbstractUser):
    email = models.EmailField(blank=False)
    # gender = models.BooleanField(default=True)
    age = models.CharField(
        max_length=20,
        choices=AGECHOICE
    )
    height = models.FloatField()
    weight = models.FloatField()
    target_weight = models.FloatField()

    REQUIRED_FIELDS = ["email", "age", "height", "weight","target_weight"]

    def __str__(self):
        return self.username
    
    def reach_target(self):
        if self.weight > self.target_weight:
            return self.weight - self.target_weight
        
        elif self.weight < self.target_weight:
            return self.target_weight - self.weight

    def get_bmi(self):
        return self.weight / ((self.height / 100) * (self.height / 100))
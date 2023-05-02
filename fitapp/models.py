from django.db import models
from django.contrib.auth.models import AbstractUser

AGECHOICE = (('young','10~20'),('youngn adult','20~30'),('adult','30~40'),('senior','40~50'))

HEIGHTCHOICE = ('low','140cm~150cm'),('middle','150cm~160cm'),('high', '160cm~170cm'),('super', '170cm~180cm'),

class CustomUser(AbstractUser):
    email = models.EmailField(blank=False)
    gender = models.BooleanField(default=True)
    age = models.CharField(
        max_length=20,
        choices=AGECHOICE
    )
    height = models.CharField(
        max_length=20,
        choices=HEIGHTCHOICE
    )
    weight = models.FloatField()
    target_weight = models.FloatField()

    REQUIRED_FIELDS = ["email", "gender", "age", "height", "weight","target_weight"]

    def __str__(self):
        return self.username
    
    def get_bmi(self):
        """Return the bmi for the user."""
        return self.weight / ((self.height / 100) * (self.height / 100))
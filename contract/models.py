from django.db import models


class Contract(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.name

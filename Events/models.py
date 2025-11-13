from django.db import models

class Event(models.Model):
    EVENT_TYPES = [
        ('Mendi', 'Mendi'),
        ('Barat', 'Barat'),
        ('Walima', 'Walima'),
    ]

    HALL_CHOICES = [
        ('Rose', 'Rose'),
        ('Jasmine', 'Jasmine'),
        ('Tulip', 'Tulip'),
    ]

    TIME_SLOTS = [
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    ]

    event_id = models.IntegerField(primary_key=True, unique=True)
    event_date = models.DateField()
    client_name = models.CharField(max_length=100)
    hall = models.CharField(max_length=20, choices=HALL_CHOICES)
    time_slot = models.CharField(max_length=20, choices=TIME_SLOTS)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    guests = models.PositiveIntegerField()
    menu = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.client_name} - {self.event_type} on {self.event_date}"

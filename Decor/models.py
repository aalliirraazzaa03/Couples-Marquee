from django.db import models
from Events.models import Event

class Decor(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='decor')
    decor_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dj_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    spotlight_count = models.IntegerField(null=True, blank=True)
    spotlight_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cool_fire_count = models.IntegerField(null=True, blank=True)
    cool_fire_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ice_pot_count = models.IntegerField(null=True, blank=True)
    ice_pot_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    confetti_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Decor for {self.event.client_name}"


class DecorImage(models.Model):
    id = models.AutoField(primary_key="Ture", unique="Ture")
    image = models.ImageField(upload_to='decor_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"